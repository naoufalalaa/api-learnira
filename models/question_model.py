from typing import List, Optional
from pydantic import BaseModel
from enum import Enum 
from models.response_model import ResponseModel

class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class QuestionModel(BaseModel):
    title: str
    description: Optional[str]
    difficulty: Difficulty
    responses: Optional[List[ResponseModel]] = None
    score: int
    
    def serial(self):
        return {
            "title": self.title,
            "description": self.description,
            "difficulty": self.difficulty,
            "responses": [response.serial() for response in self.responses],
            "score": self.score
        }

def questionModelSerial(question) -> dict:
    return {
        "id": str(question["_id"]),
        "title": question["title"],
        "description": question["description"],
        "difficulty": question["difficulty"],
        "responses": question["responses"],
        "score": question["score"]
    }

def questionsModelSerial(questions) -> list:
    return [questionModelSerial(question) for question in questions]