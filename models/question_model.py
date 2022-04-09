from typing import List, Optional
from pydantic import BaseModel

from models.response_model import ResponseModel

class QuestionModel(BaseModel):
    title: str
    description: str 
    difficulty: str
    responses: Optional[List[ResponseModel]] = None
    score: int

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