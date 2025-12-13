#AI-Powered Document Ingestion & Chat System

An AI-first backend system that allows users to upload documents, extract insights, and interact with them using natural language queries. Built with Python, Celery, and advanced AI models for efficient document processing.

Features

Upload and process documents in various formats (PDF, DOCX, TXT, etc.)

AI-based content extraction and summarization

Semantic search and retrieval from uploaded documents

RAG-based “ChatGPT for your documents” interface

Asynchronous document ingestion using Celery

Installation

Clone the repository:

git clone <your-repo-url>
cd <repo-folder>


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Set up environment variables:

Create a .env file and add your API keys or configuration:

OPENAI_API_KEY=<your-key>
REDIS_URL=redis://localhost:6379/0

Running the Project
Start Redis (for Celery backend):
redis-server

Start Celery Worker

Option 1 (Safe on macOS / avoid segmentation faults):

celery -A app.celery_app.celery_app worker --pool=solo --loglevel=info


Option 2 (Default multiprocessing pool):

celery -A app.celery_app.celery_app worker --loglevel=info

Run the App
python app/main.py

Project Structure
app/
├── celery_app/
│   ├── celery_app.py       # Celery configuration
│   └── tasks.py            # Document ingestion tasks
├── workers/
│   └── ingestion.py        # Ingestion logic
├── main.py                 # App entry point
├── utils/                  # Utility scripts
└── requirements.txt

Contributing

We are continuously working on improving this system. Contributions and new feature ideas are welcome.
Future enhancements include:

Improved document parsing for more formats

Better AI summarization and extraction techniques

Enhanced multi-document chat capabilities


❤️ Made with love by Shivansh Pareek
We will continue to work on adding new features to it.
Feel free to clone and contribute
