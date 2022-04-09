from fastapi import FastAPI, Depends, HTTPException
from auth import AuthHandler
from models.schemas import AuthDetails,authDetailsSerial,authsDetailsSerial
from config.database import users
from routes.quiz_routes import quizes_api_router


app = FastAPI()

app.include_router(quizes_api_router, prefix="/quizes", tags=["quizes"])


# USER
auth_handler = AuthHandler()


@app.post('/register', status_code=201,tags=["users"])
async def register(auth_details: AuthDetails):
    if users.find_one({'username' : auth_details.username}) is not None:
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    auth_details.password = hashed_password
    _id = users.insert_one(dict(auth_details))
    return authDetailsSerial(users.find_one({"_id": _id.inserted_id}))

@app.post('/login',tags=["users"])
async def login(auth_details: AuthDetails):
    user = users.find_one({"username": auth_details.username})
    if (user is None) or (not auth_handler.verify_password(auth_details.password , user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')

    token = auth_handler.encode_token(user['username'])
    return { 'token': token }


@app.get('/users',tags=["users"])
async def get_users():
    return authsDetailsSerial(users.find())


@app.get('/unprotected',tags=["users"])
def unprotected():
    return { 'hello': 'world' }


@app.get('/protected',tags=["users"])
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }

@app.get('/userLogedIn',tags=["users"])
def userLogedIn(username=Depends(auth_handler.auth_wrapper)):
    return users.find_one({"username": username},{'_id':0})


@app.get('/admin',tags=["users"])
def admin(username=Depends(auth_handler.auth_wrapper)):
    user = users.find_one({"username": username})
    if user['is_admin'] == True:
        return { 'name': username }
    else:
        raise HTTPException(status_code=401, detail='Not admin')

@app.put('/user/{username}',tags=["users"])
def update_user(username: str, auth_details: AuthDetails,username_in=Depends(auth_handler.auth_wrapper)):
    user = users.find_one({"username": username})
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    if (user['username'] != username_in):
        raise HTTPException(status_code=401, detail='Not authorized')
    if (auth_details.username != user['username']):
        if(users.find_one({"username": auth_details.username}) is not None):
            raise HTTPException(status_code=400, detail='Username is taken')
    if auth_details.password is not None:
        hashed_password = auth_handler.get_password_hash(auth_details.password)
        auth_details.password = hashed_password
    users.update_one({"username": username_in}, {"$set": dict(auth_details)})
    return authDetailsSerial(users.find_one({"username": auth_details.username}))


@app.delete('/user/{username}',tags=["users"])
def delete_user(username: str, username_in=Depends(auth_handler.auth_wrapper)):
    user = users.find_one({"username": username})
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    if (user['username'] != username_in):
        raise HTTPException(status_code=401, detail='Not authorized')
    users.delete_one({"username": username})
    return { 'username': username }