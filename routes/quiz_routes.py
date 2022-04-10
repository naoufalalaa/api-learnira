from fastapi import APIRouter

from models.schemas import AuthDetails,authDetailsSerial,authsDetailsSerial
from models.quiz_model import QuizModel,quizesModelSerial,quizModelSerial
from models.question_model import QuestionModel,questionModelSerial,questionsModelSerial
from models.response_model import ResponseModel,responseModelSerial,responsesModelSerial
from config.database import quizes,users

from bson import ObjectId

quizes_api_router = APIRouter()

@quizes_api_router.get("/")
async def get_quizes():
    return quizesModelSerial(quizes.find())

@quizes_api_router.get("/{id}")
async def get_quiz(id: str):
    return quizModelSerial(quizes.find_one({"_id": ObjectId(id)}))

@quizes_api_router.get("/{id}/questions",tags=["questions"])
async def get_questions(id: str):
    return quizes.find_one({"_id": ObjectId(id)})["questions"]

@quizes_api_router.post("/")
async def create_quiz(quiz: QuizModel):
    _id = quizes.insert_one(quiz.dict())
    return quizModelSerial(quizes.find_one({"_id": _id.inserted_id}))

@quizes_api_router.put("/{id}")
async def update_quiz(id: str, quiz: QuizModel):
    quizes.update_one({"_id": ObjectId(id)}, {"$set": quiz.dict()})
    return quizModelSerial(quizes.find_one({"_id": ObjectId(id)}))

@quizes_api_router.delete("/{id}")
async def delete_quiz(id: str):
    quizes.delete_one({"_id": ObjectId(id)})
    return quizModelSerial(quizes.find_one({"_id": ObjectId(id)}))

@quizes_api_router.post("/{id}/questions",tags=["questions"])
async def create_question(id: str, question: QuestionModel):
    quizes.update_one({"_id": ObjectId(id)}, {"$push": {"questions": question.dict()}})
    return quizes.find_one({"_id": ObjectId(id)})["questions"]

@quizes_api_router.get("/{id}/creator")
async def get_creator(id: str):
    username = quizes.find_one({"_id": ObjectId(id)})["creator"]
    return users.find_one({"username": username},{"_id": 0,"password": 0,"email": 0})

