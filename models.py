from pydantic import BaseModel
from typing import List, Optional

class Proposal(BaseModel):
    id: str
    title: str
    body: str
    choices: List[str]
    scores: List[int]
