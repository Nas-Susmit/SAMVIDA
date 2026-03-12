# SAMVIDA – AI‑Driven Collaborative Software Development Pod

SAMVIDA simulates a full software development team using specialized AI agents. Given a plain‑English project idea, it produces user stories, system design, production‑ready code (FastAPI + React), automated tests, and commits everything to GitHub – all within minutes.

## ✨ Features
- **Multi‑agent orchestration**: Business Analyst, Design, Developer, Testing agents.
- **AI‑powered generation**: Uses Google Gemini (with Groq fallback) for realistic artifacts.
- **Full‑stack output**: Backend (FastAPI, SQLAlchemy) and frontend (React) code.
- **Automated testing**: Pytest & Jest integration with real test execution.
- **GitHub integration**: Every agent run commits and pushes changes.
- **Chat interface**: Interact via a React chat UI (or Telegram bot with n8n).

## 🏗️ Project Structure

samvida/
├── backend/ # SAMVIDA backend (FastAPI, agents, test runner)
│ ├── agents.py # AI agent classes
│ ├── bot.py # Project Lead Bot
│ ├── database.py # SQLite models
│ ├── github_integration.py
│ ├── test_runner.py
│ └── requirements.txt
├── frontend/ # SAMVIDA chat UI (React)
│ ├── public/
│ ├── src/
│ └── package.json
├── templates/ # Markdown templates for artifacts
├── workspace/ # Generated projects (optional, gitignored)
└── README.md


## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Git
- (Optional) Docker for n8n

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
cp .env.example .env       # add your API keys
uvicorn main:app --reload

### Frontend Setup (Chat UI)
```bash

cd frontend
npm install
npm start

Open http://localhost:3000 and start chatting with the bot.

### Environment Variables

Create a .env file in backend/:
GEMINI_API_KEY=your_key
GROQ_API_KEY=your_key
GITHUB_TOKEN=your_token
GITHUB_REPO_URL=https://github.com/yourusername/your-repo.git

### 📖 Usage
Type commands in the chat interface:

/start Build a task manager... – initialise a project.

/show user_stories – view generated stories.

/rerun design – regenerate design.

/run_tests – execute tests.

/status – check artifact timestamps.

### 🤖 How It Works

1. User submits requirements.

2. Business Analyst Agent → user stories.

3. Design Agent → system architecture.

4. Developer Agent → full‑stack code.

5. Testing Agent → tests & report.

6. All artifacts are saved locally and committed to GitHub.


### 🧪 Testing the Generated Project

After /rerun dev, navigate to workspace/ and run:

cd workspace/backend
pip install -r requirements.txt
uvicorn main:app --reload

# In another terminal
cd workspace/frontend
npm install
npm start

### 📊 Visual Dashboard with n8n

For a visual representation of the agent workflow, import the provided n8n workflow (see n8n/ folder) and run it with Docker.

### 👥 Contributors

Susmit Naskar [Github: Nas-Susmit]

