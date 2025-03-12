from pymongo import MongoClient
from config import MONGO_URI

# Initialize MongoDB Client
client = MongoClient(MONGO_URI)
db = client.get_database()  # Get default database from URI

# Collections
proposals_collection = db["proposals"]
