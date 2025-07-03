# test_connection.py
from pymongo import MongoClient

client = MongoClient("mongodb+srv://mariadeeptitt:jfYrMQ7vx1W1p2nz@studybuddy.di8q2hn.mongodb.net/?retryWrites=true&w=majority&appName=studybuddy")
db = client["studybuddy_ai"]
collection = db["users"]

print("Connection successful!")
print("Total users:", collection.count_documents({}))
