```markdown
# SAMVIDA – AI-Driven Collaborative Software Development Pod

SAMVIDA is an AI-powered multi-agent system that simulates a collaborative software development team.  
Given a plain-English project idea, SAMVIDA automatically transforms it into **structured user stories, system architecture, production-ready code, and automated tests** within minutes.

The platform orchestrates multiple specialized AI agents that work together to replicate the **Software Development Life Cycle (SDLC)**. Each agent performs a specific role such as requirement analysis, architecture design, development, and testing.

The system is built with a **FastAPI backend, React frontend, AI agent orchestration, and automated GitHub integration**, making it capable of generating and managing complete software projects autonomously.

---

# ✨ Features

### Multi-Agent Orchestration
SAMVIDA coordinates multiple specialized AI agents that simulate a real development team:

- **Business Analyst Agent** – Converts requirements into structured user stories.
- **Design Architect Agent** – Generates system architecture and technical design.
- **Developer Agent** – Produces full-stack code based on the architecture.
- **Testing Agent** – Performs code analysis and generates automated tests.

### AI-Powered Artifact Generation
SAMVIDA uses modern Large Language Models to generate realistic software artifacts including:

- Requirements analysis
- User stories
- Architecture documentation
- Production-ready code
- Automated test cases

The system integrates **Google Gemini models with Groq as a fallback provider** to ensure reliable AI responses.

### Full-Stack Code Generation
The platform generates a complete application stack:

Backend
- FastAPI
- SQLAlchemy ORM
- REST APIs
- Modular project structure

Frontend
- React
- Component-based architecture
- API integration with backend

### Automated Testing
SAMVIDA automatically generates and executes tests for the generated application.

Testing frameworks used:
- **Pytest** for backend testing
- **Jest** for frontend testing

This ensures the generated code is **validated and production-ready**.

### GitHub Integration
All generated artifacts are automatically committed and pushed to GitHub.  
This provides:

- Version control
- Automatic project repository creation
- Traceability of AI-generated development artifacts

### Interactive Chat Interface
Users can interact with SAMVIDA using a **chat-based interface** built with React.

Optional integrations include:

- Telegram bot interface
- Workflow visualization using n8n

---

# 🏗️ Project Structure

```

samvida/
├── backend/                     # SAMVIDA backend (FastAPI, AI agents, test runner)
│   ├── agents.py                # AI agent implementations
│   ├── bot.py                   # Project Lead Bot orchestrating agents
│   ├── database.py              # SQLite database models
│   ├── github_integration.py    # GitHub commit and push automation
│   ├── test_runner.py           # Automated test execution system
│   ├── main.py                  # FastAPI entry point
│   └── requirements.txt
│
├── frontend/                    # React chat interface
│   ├── public/
│   ├── src/
│   └── package.json
│
├── templates/                   # Markdown templates for AI-generated artifacts
│
├── workspace/                   # Generated projects (auto-created, gitignored)
│
└── README.md

````

---

# 🚀 Quick Start

## Prerequisites

Ensure the following are installed on your system:

- Python **3.10+**
- Node.js **18+**
- Git
- (Optional) Docker for running n8n workflows

---

# Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
# Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env

# Add your API keys inside .env

uvicorn main:app --reload
````

The backend server will start at:

```
http://localhost:8000
```

---

# Frontend Setup (Chat Interface)

```bash
cd frontend

npm install

npm start
```

Open your browser and navigate to:

```
http://localhost:3000
```

You can now interact with SAMVIDA using the chat interface.

---

# Environment Variables

Create a `.env` file inside the **backend/** directory.

```
GEMINI_API_KEY=your_gemini_key

GROQ_API_KEY=your_groq_key

GITHUB_TOKEN=your_github_token

GITHUB_REPO_URL=https://github.com/yourusername/your-repo.git
```

These keys enable:

* AI model interaction
* GitHub repository automation
* Artifact generation

---

# 📖 Usage

You can interact with SAMVIDA using chat commands.

Example commands:

```
/start Build a task manager application
```

Initializes a new project pipeline.

```
/show user_stories
```

Displays generated user stories.

```
/rerun design
```

Regenerates the architecture design.

```
/run_tests
```

Runs automated tests for the generated code.

```
/status
```

Shows the status and timestamps of generated artifacts.

---

# 🤖 How It Works

SAMVIDA follows a structured multi-agent workflow that mirrors a real software development process.

### 1. Requirement Input

The user submits a plain-English project idea through the chat interface.

### 2. Business Analyst Agent

The requirement is analyzed and converted into structured **user stories** representing functional requirements.

### 3. Design Architect Agent

The user stories are transformed into **system architecture**, defining:

* Application structure
* Technology stack
* Component interactions

### 4. Developer Agent

Using the architecture specification, the developer agent generates:

* Backend APIs
* Database models
* Frontend components
* Project configuration

### 5. Testing Agent

The generated code is analyzed for potential issues and **automated test cases** are created.

### 6. GitHub Commit

All generated artifacts are stored locally and automatically committed to the configured GitHub repository.

---

# 🧪 Testing the Generated Project

After running the development pipeline, a generated project will appear inside the **workspace/** directory.

To run the generated application:

Backend:

```bash
cd workspace/backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Frontend:

```bash
cd workspace/frontend

npm install

npm start
```

This launches the full generated application locally.

---

# 📊 Visual Workflow Dashboard (Optional)

SAMVIDA also supports visual workflow monitoring using **n8n automation workflows**.

The workflow demonstrates how AI agents interact across the development lifecycle including:

* Requirement analysis
* User story generation
* Architecture creation
* Code generation
* Automated testing
* Artifact logging

To run the workflow:

1. Import the provided workflow file into n8n.
2. Configure API credentials.
3. Execute the workflow to observe the agent pipeline.

---

# 👥 Contributors

**Susmit Naskar**

GitHub
[https://github.com/Nas-Susmit](https://github.com/Nas-Susmit)

```


These **increase the chances of recruiters noticing your repo.**
```
