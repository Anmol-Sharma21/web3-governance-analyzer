import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config import JWT_SECRET_KEY
from database import users_collection

def create_user(username, email, password):
    """Registers a new user."""
    hashed_pw = generate_password_hash(password)
    user = {"username": username, "email": email, "password": hashed_pw}
    users_collection.insert_one(user)
    return {"message": "User created successfully"}

def authenticate_user(email, password):
    """Validates user credentials & returns a JWT token."""
    user = users_collection.find_one({"email": email})
    if not user or not check_password_hash(user["password"], password):
        return None

    payload = {"email": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)}
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return token
