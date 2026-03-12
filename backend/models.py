from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class Message(BaseModel):
    role: str  # "user" or "bot"
    content: str

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    artifacts: Optional[Dict[str, Any]] = None

class AgentTrigger(BaseModel):
    agent: str  # "ba", "design", "dev", "test"
    input: Optional[str] = None