from flask import Blueprint, request, jsonify
from services.dao_service import submit_proposal, vote_on_proposal, analyze_proposal
from database import proposals_collection

proposals_bp = Blueprint("proposals", __name__)

@proposals_bp.route("/submit", methods=["POST"])
def submit():
    data = request.json
    return jsonify(submit_proposal(data["title"], data["body"], data["choices"]))

@proposals_bp.route("/vote", methods=["POST"])
def vote():
    data = request.json
    return jsonify(vote_on_proposal(data["proposal_id"], data["user_id"], data["vote_choice"]))

@proposals_bp.route("/analyze", methods=["GET"])
def analyze():
    proposal = proposals_collection.find_one({}, {"_id": 0})  # Get latest proposal
    if not proposal:
        return jsonify({"error": "No proposals found"}), 404
    return jsonify(analyze_proposal(proposal))
