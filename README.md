# AI Travel Planner (Multi-Agent Conversational System)

An intelligent multi-agent AI Travel Planning system built using:

- Streamlit (Frontend UI)
- CrewAI (Multi-Agent Orchestration)
- MySQL (Persistent Multi-Session Memory)
- Python

This project implements a ChatGPT-style conversational interface with multi-session support and persistent database memory.

---

## Features

- Multi-session ChatGPT-style interface
- Persistent conversation memory using MySQL
- Auto session title generation (based on first message)
- AI itinerary generation
- Hotel recommendation agent
- Budget optimization agent
- Sidebar session switching
- Restart-safe memory persistence
- Environment variable configuration (.env)

---

## High Level Architecture

The system follows a layered modular architecture:

### Presentation Layer
- Streamlit UI
- Chat interface
- Sidebar session management

### Controller Layer
- `app.py` (Main orchestration controller)

### Service Layer
- `travel_service.py`
- Intelligent routing logic

### Agent Layer
- Travel Agent
- Hotel Agent
- Budget Agent
- CrewAI Orchestrator

### Persistence Layer
- MySQL Database
- Session Management
- Chat Memory Storage

---

## Database Schema

###  sessions Table

| Column      | Type        | Description |
|------------|------------|------------|
| id         | VARCHAR     | Primary Key (UUID) |
| title      | VARCHAR     | Chat title |
| created_at | TIMESTAMP   | Creation time |

---

###  chat_memory Table

| Column      | Type        | Description |
|------------|------------|------------|
| id         | INT         | Primary Key (Auto Increment) |
| session_id | VARCHAR     | Foreign Key (sessions.id) |
| role       | VARCHAR     | user / assistant |
| message    | TEXT        | Chat content |
| created_at | TIMESTAMP   | Message timestamp |

---

##  Setup Instructions

### 1️ Clone Repository

```bash
git clone <your-repository-url>
cd <project-folder>

### Create Virtual Environment

python -m venv venv

Activate environment:

Mac/Linux
source venv/bin/activate

Windows
venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt