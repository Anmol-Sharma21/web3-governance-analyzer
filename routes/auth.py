from flask import Blueprint, request, jsonify
from services.auth_service import create_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    return jsonify(create_user(data["username"], data["email"], data["password"]))

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    token = authenticate_user(data["email"], data["password"])
    if not token:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"token": token})
