import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Ensure required variables are set
if not MONGO_URI:
    raise ValueError("Missing MONGO_URI in .env")
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env")
