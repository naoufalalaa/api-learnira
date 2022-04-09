from typing import List, Optional
from pydantic import BaseModel
from models.question_model import QuestionModel

class QuizModel(BaseModel):
    title: str
    description: str
    creator: str
    createdAt: str
    questions: Optional[List[QuestionModel]] = None


def quizModelSerial(quiz) -> dict:
    return {
        "id": str(quiz["_id"]),
        "title": quiz["title"],
        "description": quiz["description"],
        "creator": quiz["creator"],
        "createdAt": quiz["createdAt"]
    }

def quizesModelSerial(quizes) -> list:
    return [quizModelSerial(quiz) for quiz in quizes]