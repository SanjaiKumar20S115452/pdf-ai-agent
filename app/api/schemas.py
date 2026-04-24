from pydantic import BaseModel, Field
from typing import List

class AskRequest(BaseModel):
    question: str = Field(..., description="User question about private documents")
    session_id: str = Field(default="default", description="Conversation session ID")
    
class SourceChunk(BaseModel):
    source: str
    content: str
    
class AskResponse(BaseModel):
    question: str
    answer: str
    sources: List[SourceChunk]