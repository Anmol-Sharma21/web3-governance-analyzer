from flask import Blueprint, jsonify
from services.dao_service import fetch_proposals, analyze_proposal

proposals_bp = Blueprint("proposals", __name__)

@proposals_bp.route("/proposals", methods=["GET"])
def get_proposals():
    proposals = fetch_proposals()
    return jsonify({"status": "success", "data": proposals})

@proposals_bp.route("/analyze", methods=["POST"])
def analyze():
    proposals = fetch_proposals()
    if not proposals:
        return jsonify({"status": "error", "message": "No proposals found."}), 404

    result = analyze_proposal(proposals[0])  # Analyze first proposal
    return jsonify({"status": "success", "data": result})
