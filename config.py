import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# MongoDB Config
MONGO_URI = os.getenv("MONGO_URI")

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# Validate Config
if not all([MONGO_URI, GROQ_API_KEY, JWT_SECRET_KEY]):
    raise ValueError("Missing required environment variables in .env!")
