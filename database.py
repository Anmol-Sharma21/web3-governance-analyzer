from pymongo import MongoClient
from config import MONGO_URI

# MongoDB Client
client = MongoClient(MONGO_URI)
db = client.get_database()

# Collections
proposals_collection = db["proposals"]
users_collection = db["users"]
votes_collection = db["votes"]
