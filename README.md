# ResearchDesk — 3D Multi-Agent AI Research Assistant

**ResearchDesk** (`sovon410/researchdesk-multi-agent-ai`) is a full-stack multi-agent AI research platform built with **Agno**, **Flask**, **Ollama / NVIDIA NIM**, and a self-contained **3D WebGL / Three.js** frontend. A central **Research Team** coordinator (`gpt-oss:120b`) analyzes incoming queries and dynamically delegates tasks across five specialized AI agents (`gemma4:31b-cloud`) equipped with real-time web search, deep webpage extraction, Yahoo Finance market data, YouTube transcript analysis, and browser automation tools.

---

## Key Highlights

- **Coordinated 5-Agent Agno Architecture**: A central `Research Team` coordinator (`backend/teams/research_team.py`) delegates tasks to specialized member agents and synthesizes their findings into a unified, source-backed Markdown response.
- **Real-Time Plain-Text Streaming**: The Flask backend (`backend/main.py`) exposes both standard JSON (`POST /api/chat`) and low-latency streaming (`POST /api/chat/stream`) endpoints using `stream_with_context`.
- **Single-File 3D Neural Frontend (`frontend/index.html`)**: Built entirely with vanilla HTML5, CSS3, and JavaScript (no build step, bundler, or Node.js required) featuring a Three.js 3D neural network, orbiting agent nodes, synaptic data pulses, 3D perspective-tilt cards, `AbortController` stream cancellation, `localStorage` session persistence, Dark/Light themes, and a 2D SVG fallback when WebGL is unavailable.
- **Flexible Model Provider Layer (`backend/config.py`)**: Configured out-of-the-box for **Ollama** (`gpt-oss:120b` and `gemma4:31b-cloud`) with ready-to-uncomment **NVIDIA NIM** model adapters (`google/gemma-4-31b-it`, `openai/gpt-oss-20b`, `z-ai/glm-5.3-flash`, `deepseek-ai/deepseek-v4.1-flash`, and `minimaxai/minimax-m3.1-flash`).

---

## System Architecture & Multi-Agent Roster

### 1. Coordinator Team (`backend/teams/research_team.py`)

| Component | Name | Default Model | Responsibility |
| :--- | :--- | :--- | :--- |
| **Team Coordinator** | `Research Team` | `Ollama(id="gpt-oss:120b")` (`ollama-gpt`) | Analyzes user intent, routes subtasks to matching member agents, enforces citation grounding, and merges member outputs into one cohesive Markdown response. |

### 2. Specialized Member Agents (`backend/agents/`)

| Agent Name | Source File | Default Model | Agno Toolset | Core Role & Delegation Rule |
| :--- | :--- | :--- | :--- | :--- |
| **Search Agent** | `backend/agents/search_agent.py` | `gemma4:31b-cloud` (`ollama-gemma`) | `DuckDuckGoTools(timeout=30, fixed_max_results=3)` | Finds breaking news, current events, and general facts (`Asia/Kolkata` timezone context) with source URLs. |
| **Web Researcher** | `backend/agents/web_researcher.py` | `gemma4:31b-cloud` (`ollama-gemma`) | `WebSearchTools(backend="auto", fixed_max_results=5)`, `WebsiteTools()` | Reads and extracts detailed information from discovered or user-supplied URLs without fabricating links. |
| **Finance Agent** | `backend/agents/finance_agent.py` | `gemma4:31b-cloud` (`ollama-gemma`) | `YFinanceTools()` | Resolves stock tickers and presents share prices, market cap, P/E ratios, fundamentals, and analyst data in Markdown tables. |
| **YouTube Agent** | `backend/agents/youtube_agent.py` | `gemma4:31b-cloud` (`ollama-gemma`) | `YouTubeTools()` | Fetches YouTube video metadata, captions, and transcripts, summarizing key takeaways with approximate timestamps. |
| **Browser Agent** | `backend/agents/browser_agent.py` | `gemma4:31b-cloud` (`ollama-gemma`) | `WebBrowserTools()` | Opens target web pages directly in the user's default browser when explicitly requested and confirms the opened URL. |

---

## Repository Structure

| Path | Description |
| :--- | :--- |
| `backend/__init__.py` | Marks `backend` as a Python package so modules can be executed via `python -m backend.main`. |
| `backend/.env.example` | Template environment variables file (`NVIDIA_API_KEY`, `OLLAMA_API_KEY`). |
| `backend/config.py` | Abstract `Model` factory and `SelectModel` registry for Ollama (`ollama-gpt`, `ollama-gemma`) and NVIDIA NIM models. |
| `backend/main.py` | Flask application entrypoint serving `/api/health`, `/api/chat`, and `/api/chat/stream` on `http://127.0.0.1:5000`. |
| `backend/teams/__init__.py` | Exports `ResearchTeam`. |
| `backend/teams/research_team.py` | Defines the 5-agent Agno `Team`, coordinator model, and routing instructions. |
| `backend/agents/__init__.py` | Exports `BrowserAgent`, `FinanceAgent`, `SearchAgent`, `WebResearcher`, and `YouTubeAgent`. |
| `backend/agents/browser_agent.py` | Agno `Browser Agent` implementation using `WebBrowserTools`. |
| `backend/agents/finance_agent.py` | Agno `Finance Agent` implementation using `YFinanceTools`. |
| `backend/agents/search_agent.py` | Agno `Search Agent` implementation using `DuckDuckGoTools`. |
| `backend/agents/web_researcher.py` | Agno `Web Researcher` implementation using `WebSearchTools` and `WebsiteTools`. |
| `backend/agents/youtube_agent.py` | Agno `YouTube Agent` implementation using `YouTubeTools`. |
| `frontend/index.html` | Self-contained 3D glassmorphic frontend application (HTML5, CSS3, Vanilla JS, Three.js, Lucide Icons). |
| `requirements.txt` | Python package dependencies (`flask`, `flask-cors`, `agno`, `ollama`, `yfinance`, `ddgs`, `youtube-transcript-api`, `beautifulsoup4`, `google-genai`, `openai`, `python-dotenv`, `streamlit`, `setuptools`). |

---

## Prerequisites (All Devices)

Before running **ResearchDesk**, install **Python 3.10+**, **Git**, and **Ollama** on your device.

### 1. Install Python, Git, and Ollama by Operating System

#### Windows (PowerShell / Winget)
```powershell
winget install -e --id Python.Python.3.11
winget install -e --id Git.Git
winget install -e --id Ollama.Ollama
```

#### macOS (Homebrew)
```bash
brew install python@3.11 git
brew install --cask ollama
```

#### Linux (Ubuntu / Debian)
```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
curl -fsSL https://ollama.com/install.sh | sh
```

#### Linux (Fedora / RHEL)
```bash
sudo dnf install -y python3 python3-pip git curl
curl -fsSL https://ollama.com/install.sh | sh
```

#### Linux (Arch Linux)
```bash
sudo pacman -S --noconfirm python python-pip git curl ollama
```

#### Android (Termux) / Chromebook (Linux Environment)
```bash
pkg update && pkg upgrade -y
pkg install -y python git curl ollama
```

---

### 2. Pull the Required Ollama Models (All Devices)

Start the Ollama service and pull the coordinator and agent models defined in `backend/config.py`:

```bash
# Start Ollama server (if not already running as a background service)
ollama serve

# In a new terminal, pull the Coordinator model and Agent model
ollama pull gpt-oss:120b
ollama pull gemma4:31b-cloud

# Verify installed models
ollama list
```

> **Tip for Low-VRAM / Laptop Devices:** If your device does not have enough memory for `gpt-oss:120b` or `gemma4:31b-cloud`, you can either use Ollama Cloud (`OLLAMA_API_KEY`), uncomment the **NVIDIA NIM** cloud models in `backend/config.py` with `NVIDIA_API_KEY`, or change the model IDs in `backend/config.py` to a lighter local model such as `gemma3:4b` or `llama3.2:3b`.

---

## Step-by-Step Setup & Installation (For Every Device)

### Option A: Windows (PowerShell)

```powershell
# 1. Clone the repository
git clone https://github.com/sovon410/researchdesk-multi-agent-ai.git
cd researchdesk-multi-agent-ai

# 2. Create and activate a Python virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# If PowerShell blocks script execution, run this once and re-run Activate.ps1:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 3. Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Create the backend/.env file from the example template
Copy-Item backend\.env.example backend\.env

# 5. Start the Flask backend server on http://127.0.0.1:5000
python -m backend.main
```

To launch the frontend on **Windows (PowerShell)**, open a second terminal window in the project root:

```powershell
# Option 1: Open frontend/index.html directly in your default browser
Start-Process "frontend\index.html"

# Option 2: Serve frontend/index.html over a clean local HTTP port (http://127.0.0.1:8080)
python -m http.server 8080 --directory frontend
```

---

### Option B: Windows (Command Prompt / `cmd.exe`)

```cmd
:: 1. Clone the repository
git clone https://github.com/sovon410/researchdesk-multi-agent-ai.git
cd researchdesk-multi-agent-ai

:: 2. Create and activate a Python virtual environment
python -m venv .venv
.venv\Scriptsctivate.bat

:: 3. Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

:: 4. Create the backend\.env file from the example template
copy backend\.env.example backend\.env

:: 5. Start the Flask backend server on http://127.0.0.1:5000
python -m backend.main
```

To launch the frontend on **Windows (`cmd.exe`)**, open a second Command Prompt window:

```cmd
:: Option 1: Open directly in your default browser
start frontend\index.html

:: Option 2: Serve via Python HTTP server on http://127.0.0.1:8080
python -m http.server 8080 --directory frontend
```

---

### Option C: macOS (zsh / bash)

```bash
# 1. Clone the repository
git clone https://github.com/sovon410/researchdesk-multi-agent-ai.git
cd researchdesk-multi-agent-ai

# 2. Create and activate a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Upgrade pip and install dependencies
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Create the backend/.env file from the example template
cp backend/.env.example backend/.env

# 5. Start the Flask backend server on http://127.0.0.1:5000
python3 -m backend.main
```

To launch the frontend on **macOS**, open a second terminal tab:

```bash
# Option 1: Open frontend/index.html directly in your default browser
open frontend/index.html

# Option 2: Serve via Python HTTP server on http://127.0.0.1:8080 and open in browser
python3 -m http.server 8080 --directory frontend
```

---

### Option D: Linux (Ubuntu, Debian, Fedora, Arch) & Chromebook

```bash
# 1. Clone the repository
git clone https://github.com/sovon410/researchdesk-multi-agent-ai.git
cd researchdesk-multi-agent-ai

# 2. Create and activate a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Upgrade pip and install dependencies
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Create the backend/.env file from the example template
cp backend/.env.example backend/.env

# 5. Start the Flask backend server on http://127.0.0.1:5000
python3 -m backend.main
```

To launch the frontend on **Linux**, open a second terminal tab:

```bash
# Option 1: Open frontend/index.html in your default desktop browser
xdg-open frontend/index.html

# Option 2: Serve via Python HTTP server on http://127.0.0.1:8080
python3 -m http.server 8080 --directory frontend
```

---

## Environment Variables & Model Configuration

The backend loads environment variables from `backend/.env` (`backend/config.py`).

```ini
# backend/.env
NVIDIA_API_KEY=your_nvidia_nim_api_key_here
OLLAMA_API_KEY=your_ollama_cloud_api_key_here
```

### Switching Between Ollama and NVIDIA NIM Models (`backend/config.py`)

By default, `SelectModel` in `backend/config.py` registers:

- `"ollama-gpt"` → `Ollama(id="gpt-oss:120b")` (used by `ResearchTeam` in `backend/teams/research_team.py`)
- `"ollama-gemma"` → `Ollama(id="gemma4:31b-cloud")` (used by all 5 agents in `backend/agents/*.py`)

To use **NVIDIA NIM** models (`https://integrate.api.nvidia.com/v1`), uncomment the adapter classes in `backend/config.py`:

| Key in `SelectModel` | Class Name | Model ID | Provider Base URL |
| :--- | :--- | :--- | :--- |
| `"gemma"` | `ModelGemma` | `google/gemma-4-31b-it` | `https://integrate.api.nvidia.com/v1` |
| `"gpt"` | `ModelGPTOSS` | `openai/gpt-oss-20b` | `https://integrate.api.nvidia.com/v1` |
| `"glm"` | `ModelGLMFlash` | `z-ai/glm-5.3-flash` | `https://integrate.api.nvidia.com/v1` |
| `"deepseek"` | `ModelDeepseekFlash` | `deepseek-ai/deepseek-v4.1-flash` | `https://integrate.api.nvidia.com/v1` |
| `"minimax"` | `ModelMinimax` | `minimaxai/minimax-m3.1-flash` | `https://integrate.api.nvidia.com/v1` |

---

## REST API Reference (`http://127.0.0.1:5000`)

The Flask backend (`backend/main.py`) runs with `CORS(app)` and `threaded=True` on `http://127.0.0.1:5000`.

### 1. Health Check — `GET /api/health`

Verifies that the Flask server and Agno `ResearchTeam` instance are online.

- **Response (`200 OK`)**:
  ```json
  {
    "status": "ok"
  }
  ```

### 2. Synchronous Chat — `POST /api/chat`

Runs the full `ResearchTeam` workflow synchronously and returns the final Markdown response in a JSON object.

- **Request Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "message": "Find the latest news on NVIDIA and give me its current stock overview."
  }
  ```
- **Response (`200 OK`)**:
  ```json
  {
    "reply": "### NVIDIA (NVDA) Market & News Synthesis
..."
  }
  ```
- **Error Responses**:
  - `400 Bad Request`: `{"error": "message is required"}`
  - `500 Internal Server Error`: `{"error": "<exception details>"}`

### 3. Streaming Chat — `POST /api/chat/stream`

Streams plain-text chunks (`mimetype="text/plain"`) directly from `team.run(message, stream=True)` as each member agent and coordinator token is generated.

- **Request Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "message": "Make a quick research on RAG and include source URLs."
  }
  ```
- **Response (`200 OK`, `Content-Type: text/plain`)**: Raw streaming Markdown text consumed via `response.body.getReader()` and `TextDecoder`.

---

## Testing API Endpoints from the Command Line

### macOS / Linux / Git Bash (`curl`)

```bash
# 1. Check Backend Health
curl -X GET http://127.0.0.1:5000/api/health

# 2. Test Standard POST /api/chat
curl -X POST http://127.0.0.1:5000/api/chat   -H "Content-Type: application/json"   -d '{"message": "What is NVIDIA current stock price and P/E ratio?"}'

# 3. Test Streaming POST /api/chat/stream
curl -N -X POST http://127.0.0.1:5000/api/chat/stream   -H "Content-Type: application/json"   -d '{"message": "Find the latest news on NVIDIA and give me its current stock overview."}'
```

### Windows PowerShell (`Invoke-RestMethod`)

```powershell
# 1. Check Backend Health
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/health" -Method Get

# 2. Test Standard POST /api/chat
$body = @{ message = "What is NVIDIA current stock price and P/E ratio?" } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/chat" -Method Post -ContentType "application/json" -Body $body

# 3. Test Streaming POST /api/chat/stream using curl.exe on Windows
curl.exe -N -X POST "http://127.0.0.1:5000/api/chat/stream" -H "Content-Type: application/json" -d "{\`"message\`": \`"Make a quick research on RAG.\`"}"
```

---

## Testing Individual Agents via CLI

You can also test each specialized agent or the coordinator team directly from the terminal without starting Flask:

```bash
# Test Search Agent directly
python -m backend.agents.search_agent

# Test Finance Agent (uncomment the __main__ block in backend/agents/finance_agent.py)
python -m backend.agents.finance_agent

# Test Web Researcher (uncomment the __main__ block in backend/agents/web_researcher.py)
python -m backend.agents.web_researcher

# Test YouTube Agent (uncomment the __main__ block in backend/agents/youtube_agent.py)
python -m backend.agents.youtube_agent

# Test Browser Agent (uncomment the __main__ block in backend/agents/browser_agent.py)
python -m backend.agents.browser_agent

# Test the full 5-Agent Research Team Coordinator (uncomment __main__ in backend/teams/research_team.py)
python -m backend.teams.research_team
```

---

## Frontend Architecture & Features (`frontend/index.html`)

The frontend adheres strictly to a **zero-build, single-file architecture** inside `frontend/index.html`:

- **Three.js 3D Neural Network Stage**:
  - Central glowing icosahedron representing the **Research Team Coordinator** (`gpt-oss:120b`).
  - Five orbiting octahedral nodes representing **Search Agent**, **Web Researcher**, **Finance Agent**, **YouTube Agent**, and **Browser Agent** (`gemma4:31b-cloud`), linked by live synaptic lines and animated pulse packets.
  - Drag-to-orbit camera controls, raycasted node clicking, camera reset, synaptic wave trigger, and an automatic 2D SVG topology fallback when WebGL is disabled or unavailable.
- **Interactive 3D Perspective-Tilt Agent Cards**:
  - Hovering over any of the five agent cards applies a real-time 3D perspective tilt; clicking an agent card focuses that agent for delegation and highlights its 3D node in the neural network.
- **Streaming & AbortController Support**:
  - Uses `fetch()`, `response.body.getReader()`, `TextDecoder`, and `AbortController` to render plain-text streaming tokens in real time with a one-click **Stop Generation** button.
  - Includes a topbar toggle to switch between `POST /api/chat/stream` and `POST /api/chat`, plus an on-demand simulated stream preview mode when testing the UI offline.
- **Session History & Markdown Export**:
  - Automatically persists chat sessions to `localStorage` with instant session search, session deletion, and one-click `.md` report export.
- **Theme & Accessibility Controls**:
  - Instant Dark/Light theme toggle and a Reduced Motion mode that respects OS-level `prefers-reduced-motion` settings and pauses WebGL rendering when the browser tab is inactive.

---

## Troubleshooting

| Symptom | Cause | Solution |
| :--- | :--- | :--- |
| `ModuleNotFoundError: No module named 'backend'` | Running `python backend/main.py` instead of running as a module from the root directory. | Always run `python -m backend.main` from the root `researchdesk-multi-agent-ai` folder. |
| Frontend badge shows `Backend Offline (127.0.0.1:5000)` | The Flask server is not running or is blocked by another process on port 5000. | Start the server with `python -m backend.main` and click **Check Health** in the UI topbar. |
| `HTTP 500` on `/api/chat` or `/api/chat/stream` | Ollama is not running or the required models (`gpt-oss:120b`, `gemma4:31b-cloud`) have not been pulled. | Run `ollama serve` and ensure both models are available via `ollama list`, or configure `OLLAMA_API_KEY` / `NVIDIA_API_KEY` in `backend/.env`. |
| 3D Canvas shows 2D SVG Fallback | Hardware acceleration / WebGL is disabled in the browser, or fallback mode was toggled. | Click the **Layers** button in the 3D HUD to switch back to WebGL, or enable hardware acceleration in your browser settings. |
