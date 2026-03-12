import re
from .agents import BusinessAnalystAgent, DesignAgent, DeveloperAgent, TestingAgent
from .database import SessionLocal, ProjectState
import json

class ProjectBot:
    def __init__(self):
        self.ba_agent = BusinessAnalystAgent()
        self.design_agent = DesignAgent()
        self.dev_agent = DeveloperAgent()
        self.test_agent = TestingAgent()
        self.context = {}  # Store last used requirements etc.

    def process_message(self, message: str) -> str:
        message = message.strip()
        # Check for commands
        if message.startswith("/start"):
            return self._handle_start(message)
        elif message.startswith("/show"):
            return self._handle_show(message)
        elif message.startswith("/rerun"):
            return self._handle_rerun(message)
        elif message == "/run_tests":
            return self._handle_run_tests()
        elif message == "/status":
            return self._handle_status()
        else:
            return "I don't understand. Available commands: /start <requirements>, /show <artifact>, /rerun <agent>, /run_tests, /status"

    def _handle_start(self, requirements):
        self.context['requirements'] = requirements   # keep in memory for current session

        # Save to database so it survives restarts
        db = SessionLocal()
        state = db.query(ProjectState).filter_by(key="current_requirements").first()
        if state:
            state.value = requirements
        else:
            state = ProjectState(key="current_requirements", value=requirements)
            db.add(state)
        db.commit()
        db.close()

        # Trigger BA agent
        result = self.ba_agent.run(requirements)
        return f"✅ User stories created. You can view them with `/show user_stories`.\nStories: {result['stories']}"

    def _handle_show(self, msg):
        artifact = msg[5:].strip().lower()
        db = SessionLocal()
        state = db.query(ProjectState).filter_by(key=artifact).first()
        db.close()
        if state:
            # For simplicity, return the value (if JSON, pretty print)
            try:
                val = json.loads(state.value)
                return f"**{artifact}**:\n```json\n{json.dumps(val, indent=2)}\n```"
            except:
                return f"**{artifact}**:\n{state.value}"
        else:
            return f"No artifact found for '{artifact}'. Available: user_stories, design, code_generated, test_results"

    def _handle_rerun(self, msg):
        agent = msg[6:].strip().lower()
        if agent == "ba":
            # Retrieve requirements from database
            db = SessionLocal()
            req_state = db.query(ProjectState).filter_by(key="current_requirements").first()
            db.close()
            if not req_state:
                return "No previous requirements. Please run /start first."
            requirements = req_state.value
            result = self.ba_agent.run(requirements)
            return f"✅ User stories regenerated."
        elif agent == "design":
            db = SessionLocal()
            state = db.query(ProjectState).filter_by(key="user_stories").first()
            db.close()
            if not state:
                return "No user stories found. Run /start first."
            stories = json.loads(state.value)
            result = self.design_agent.run(stories)
            return f"✅ Design regenerated."
        elif agent == "dev":
            db = SessionLocal()
            state = db.query(ProjectState).filter_by(key="design").first()
            db.close()
            if not state:
                return "No design found. Run /rerun design first."
            design = json.loads(state.value)
            result = self.dev_agent.run(design)
            return f"✅ Code regenerated."
        else:
            return "Unknown agent. Use: ba, design, dev"

    def _handle_run_tests(self):
        result = self.test_agent.run()
        return f"✅ Tests executed. Results: {result['results']}"

    def _handle_status(self):
        db = SessionLocal()
        artifacts = db.query(ProjectState).all()
        db.close()
        status = []
        for a in artifacts:
            status.append(f"- {a.key}: updated at {a.updated_at}")
        return "Project status:\n" + "\n".join(status) if status else "No artifacts yet."