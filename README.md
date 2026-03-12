
# **SAMVIDA – AI-DRIVEN COLLABORATIVE SOFTWARE DEVELOPMENT POD**

samvida is an ai-driven multi-agent system designed to simulate a collaborative software development team. the platform takes a plain-english project requirement and automatically converts it into structured development artifacts such as user stories, system architecture, full-stack application code, and automated tests.

the goal of samvida is to demonstrate how ai agents can coordinate together to automate different stages of the software development life cycle (sdlc). each agent is responsible for a specific role such as requirement analysis, system design, development, and testing.

the system integrates a fastapi backend, a react chat interface, ai model integration, and automated github commits to generate and manage complete software projects with minimal human intervention.

---

# **FEATURES**

• multi-agent orchestration  
specialized ai agents simulate real software development roles including business analysis, architecture design, development, and testing.

• ai-powered artifact generation  
ai models generate development artifacts including requirements interpretation, user stories, architecture design, code, and testing reports.

• full-stack application generation  
the system generates both backend and frontend code structures.

backend technologies  
- fastapi  
- sqlalchemy  
- rest api architecture  

frontend technologies  
- react  
- component-based structure  
- api integration with backend services  

• automated testing  
samvida automatically generates test cases and validates generated code using testing frameworks.

testing frameworks used  
- pytest for backend testing  
- jest for frontend testing  

• github integration  
all generated artifacts can be automatically committed and pushed to a github repository, enabling version control and project tracking.

• interactive chat interface  
users interact with samvida through a react-based chat interface that allows them to provide requirements and monitor the development process.

---

# **PROJECT STRUCTURE**

- samvida/

- backend/  
  - agents.py – implementation of ai development agents  
  - bot.py – orchestration logic for coordinating agents  
  - database.py – sqlite database models  
  - github_integration.py – handles github commits and pushes  
  - test_runner.py – executes generated tests  
  - main.py – fastapi application entry point  
  - requirements.txt – backend dependencies  

- frontend/  
  - public/ – static assets  
  - src/ – react application source code  
  - package.json – frontend dependencies and scripts  

- templates/  
  - markdown templates used for generating structured artifacts such as user stories and design documents  

- workspace/  
  - directory where generated projects are stored during execution  

- README.md  
  - project documentation  

---

# **QUICK START**

### prerequisites

- python 3.10 or higher  
- node.js 18 or higher  
- git  
- optional: docker for running workflow automation tools  

---

# **BACKEND SETUP**

```bash
cd backend

python -m venv venv

source venv/bin/activate
# windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env

uvicorn main:app --reload
````

the backend server will run at:

[http://localhost:8000](http://localhost:8000)

---

# **FRONTEND SETUP**

```bash
cd frontend

npm install

npm start
```

open the browser and navigate to:

[http://localhost:3000](http://localhost:3000)

this launches the samvida chat interface.

---

# **ENVIRONMENT VARIABLES**

create a `.env` file inside the backend directory and configure the following variables:

```
GEMINI_API_KEY=your_key
GROQ_API_KEY=your_key
GITHUB_TOKEN=your_token
GITHUB_REPO_URL=https://github.com/yourusername/your-repo.git
```

these credentials allow samvida to communicate with ai models and push generated artifacts to github.

---

# **USAGE**

the system can be controlled through commands within the chat interface.

example commands:

```
/start build a task manager application
```

initializes the development pipeline for a new project.

```
/show user_stories
```

displays the generated user stories.

```
/rerun design
```

regenerates the architecture design.

```
/run_tests
```

executes tests for the generated project.

```
/status
```

displays the status of generated artifacts.

---

# **WORKFLOW OVERVIEW**

samvida follows a structured ai-driven development pipeline.

1. the user submits a project requirement.
2. the business analyst agent converts the requirement into structured user stories.
3. the design agent generates system architecture and technical design.
4. the developer agent produces full-stack application code.
5. the testing agent analyzes the generated code and creates automated tests.
6. generated artifacts are stored locally and optionally committed to github.

---

# **TESTING THE GENERATED PROJECT**

after running the development pipeline, the generated project will appear inside the workspace directory.

to run the generated backend:

```bash
cd workspace/backend

pip install -r requirements.txt

uvicorn main:app --reload
```

to run the generated frontend:

```bash
cd workspace/frontend

npm install

npm start
```

this launches the generated full-stack application locally.

---

# **VISUAL WORKFLOW WITH N8N**

samvida also supports workflow visualization using n8n automation pipelines.

the workflow demonstrates how ai agents collaborate across multiple stages of the software development life cycle, including requirement analysis, design generation, code creation, and automated testing.

---

# **CONTRIBUTOR**

susmit naskar
github: [https://github.com/Nas-Susmit](https://github.com/Nas-Susmit)

```

