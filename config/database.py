from pymongo import MongoClient
from dotenv import load_dotenv
import os
 
load_dotenv()

USER = os.getenv('MONGO_USER')
PASSWORD = os.getenv('MONGO_PASSWORD')
str = 'mongodb+srv://' + USER + ':' + PASSWORD + '@cluster0.oijg0.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(str)

db = client.learnira

users = db["users"]
quizes = db["Quizes"]
questions = db["questions"]
responses = db["responses"]
 

