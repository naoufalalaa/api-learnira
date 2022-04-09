from pymongo import MongoClient

client = MongoClient("mongodb+srv://user1:user1@cluster0.oijg0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.learnira

users = db["users"]
quizes = db["Quizes"]
questions = db["questions"]
responses = db["responses"]
 

