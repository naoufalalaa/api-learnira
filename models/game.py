from pydantic import BaseModel

class GameModel(BaseModel):
    username : str
    quiz_id : str 
    score : int