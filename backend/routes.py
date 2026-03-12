from fastapi import APIRouter, Depends, HTTPException
from .models import ChatRequest, ChatResponse, AgentTrigger
from .bot import ProjectBot
from .agents import BusinessAnalystAgent, DesignAgent, DeveloperAgent, TestingAgent
from .database import get_db, SessionLocal
from sqlalchemy.orm import Session
from .database import ProjectState
import json

router = APIRouter()
bot = ProjectBot()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = bot.process_message(request.message)
    return ChatResponse(response=response)

@router.post("/trigger_agent")
async def trigger_agent(trigger: AgentTrigger):
    if trigger.agent == "ba":
        agent = BusinessAnalystAgent()
        result = agent.run(trigger.input or "")
    elif trigger.agent == "design":
        agent = DesignAgent()
        # Need user stories from DB
        db = SessionLocal()
        state = db.query(ProjectState).filter_by(key="user_stories").first()
        db.close()
        if not state:
            raise HTTPException(status_code=400, detail="No user stories found")
        result = agent.run(json.loads(state.value))
    elif trigger.agent == "dev":
        agent = DeveloperAgent()
        db = SessionLocal()
        state = db.query(ProjectState).filter_by(key="design").first()
        db.close()
        if not state:
            raise HTTPException(status_code=400, detail="No design found")
        result = agent.run(json.loads(state.value))
    elif trigger.agent == "test":
        agent = TestingAgent()
        result = agent.run()
    else:
        raise HTTPException(status_code=400, detail="Invalid agent name")
    return {"message": "Agent triggered", "result": result}