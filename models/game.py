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

    def __init__(self, username, quiz_id, questions, responses, score):
        self.username = username
        self.quiz_id = quiz_id
        self.questions = questions
        self.responses = responses
        self.score = score

    def __str__(self):
        return f"{self.username} {self.quiz_id} {self.questions} {self.responses} {self.score}"
    
    def dict(self):
        return {
            "username": self.username,
            "quiz_id": self.quiz_id,
            "questions": [question.dict() for question in self.questions],
            "responses": [response.dict() for response in self.responses],
            "score": self.score
        }

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
        "questions": [question.serial() for question in game["questions"]],
        "responses": [response.serial() for response in game["responses"]],
        "score": game["score"]
    }

def gamesModelSerial(games) -> list:
    return [gameModelSerial(game) for game in games]