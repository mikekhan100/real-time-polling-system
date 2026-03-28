# Real-time Polling System (WebSockets) 🚀

A high-performance, asynchronous polling application that allows multiple users to vote and see results update instantly across all screens without page refreshes.

## 🛠️ Tech Stack

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
* **Real-time Communication:** WebSockets & [Broadcaster](https://github.com/encode/broadcaster)
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Jinja2 Templates
* **Concurrency:** Python `asyncio` & Lifespan API

## ✨ Key Features

* **Bi-directional Communication:** Uses WebSockets for a persistent, open connection between client and server.
* **Pub/Sub Architecture:** Implements a Publish/Subscribe pattern to synchronise state across multiple isolated user sessions.
* **Non-blocking I/O:** Leverages FastAPI's `async` capabilities and `asyncio.gather` to handle concurrent incoming and outgoing data streams.
* **Modern Lifespan Management:** Uses the updated FastAPI Lifespan API for clean setup and teardown of broadcast connections.

## 🚀 Getting Started

### Prerequisites
* Python 3.8+
* pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mikekhan100/real-time-polling-system.git](https://github.com/mikekhan100/real-time-polling-system.git)
   cd real-time-polling-system

2. **Create and activate a virtual environment:**
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. **Install dependencies:**
pip install -r requirements.txt

4. **Run the application:**
uvicorn main:app --reload

5. **Test it out:**
Open http://127.0.0.1:8000 in two different browser windows side-by-side

### 🧠 Skills acquired

**State Management:** How to manage an in-memory "Source of Truth" while broadcasting changes to all subscribers.

**Async Patterns:** Moving from standard Request-Response cycles to stateful, event-driven communication.

**JSON Serialisation:** Coordinating data exchange between Python dictionaries and JavaScript objects via WebSockets.