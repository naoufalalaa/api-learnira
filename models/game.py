from typing import List, Optional
from pydantic import BaseModel
from models.question_model import QuestionModel
from models.response_model import ResponseModel

class GameModel(BaseModel):
    username : str
    quiz_id : str
    questions : List[QuestionModel]
    responses : List[ResponseModel]
    score : int