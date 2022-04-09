from pydantic import BaseModel

class GameModel(BaseModel):
    username : str
    quiz_id : str
    questions : list[]
    responses : list[] 
    score : int