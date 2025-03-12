from database import proposals_collection, votes_collection
from services.llm_service import generate_llm_content

def submit_proposal(title, body, choices):
    """Stores new proposal in MongoDB."""
    proposal = {"title": title, "body": body, "choices": choices, "scores": [0] * len(choices)}
    proposals_collection.insert_one(proposal)
    return {"message": "Proposal submitted successfully"}

def vote_on_proposal(proposal_id, user_id, vote_choice):
    """Records a user's vote for a proposal."""
    valid_choices = ["support", "against", "abstain"]
    if vote_choice not in valid_choices:
        return {"error": "Invalid vote choice"}

    votes_collection.insert_one({"proposal_id": proposal_id, "user_id": user_id, "vote_choice": vote_choice})
    return {"message": "Vote recorded"}

def analyze_proposal(proposal):
    """Runs LLM analysis on the proposal."""
    summary = generate_llm_content(f"Summarize: {proposal['body']}")
    insights = generate_llm_content(f"Analyze votes: {proposal['body']}")
    return {"summary": summary, "governance_insights": insights}
