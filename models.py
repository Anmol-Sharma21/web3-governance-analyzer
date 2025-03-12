from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Proposal(BaseModel):
    id: str
    title: str
    body: str
    choices: List[str]
    scores: List[int]

class Vote(BaseModel):
    proposal_id: str
    user_id: str
    vote_choice: str  # "support", "against", "abstain"

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
