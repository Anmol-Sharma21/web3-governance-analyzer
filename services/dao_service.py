from database import proposals_collection
from services.llm_service import generate_llm_content

def fetch_proposals():
    """Fetch proposals from MongoDB"""
    return list(proposals_collection.find({}, {"_id": 0}))  # Exclude MongoDB `_id` field

def analyze_proposal(proposal):
    """Analyze and summarize the proposal"""
    proposal_text = proposal["body"]
    summary = generate_llm_content(f"Summarize this DAO proposal:\n\n{proposal_text}")
    governance_insights = generate_llm_content(f"Analyze the governance votes:\n\n{proposal_text}")
    
    return {
        "summary": summary,
        "governance_insights": governance_insights
    }
