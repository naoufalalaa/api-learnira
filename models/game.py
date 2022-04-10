from typing import List, Optional
from pydantic import BaseModel
from models.question_model import QuestionModel
from models.response_model import ResponseModel

class GameModel(BaseModel):
    username : str
    quiz_id : str
    questions : List[QuestionModel]
    responses : Optional[List[ResponseModel]] = []
    score : Optional[int] = None
    


    def serial(self):
        return {
            "username": self.username,
            "quiz_id": self.quiz_id,
            "questions": [question.serial() for question in self.questions],
            "responses": [response.serial() for response in self.responses],
            "score": self.score
        }


def gameModelSerial(game) -> dict:
    return {
        "username": game["username"],
        "quiz_id": game["quiz_id"],
        "questions": game["questions"],
        "responses": game["responses"],
        "score": game["score"]
    }

def gamesModelSerial(games) -> list:
    return [gameModelSerial(game) for game in games]