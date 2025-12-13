📄 AI-Powered Document Ingestion & Chat System

An AI-first backend that allows users to upload documents, extract insights, and chat with them naturally. Built with Python, Celery, and advanced AI models for seamless document processing.

🌟 Features

📄 Upload and process documents in various formats (PDF, DOCX, TXT, etc.)

🤖 AI-based content extraction, summarization, and semantic search

💬 Chat with your documents using natural language queries (RAG-based)

⚡ Asynchronous document ingestion using Celery for high performance

🔄 Easily extendable for new document types and AI features

🎬 Video Demo

Watch the system in action:

Click on the image to view the video demo.

🚀 Installation

Clone the repository

git clone <your-repo-url>
cd <repo-folder>


Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Set up environment variables

Create a .env file:

OPENAI_API_KEY=<your-key>
REDIS_URL=redis://localhost:6379/0

⚡ Running the Project
1. Start Redis (Celery backend):
redis-server

2. Start Celery Worker

Recommended (macOS safe / avoid segmentation faults):

celery -A app.celery_app.celery_app worker --pool=solo --loglevel=info


Default (multiprocessing pool):

celery -A app.celery_app.celery_app worker --loglevel=info

3. Run the App
python app/main.py

🗂 Project Structure
app/
├── celery_app/
│   ├── celery_app.py       # Celery configuration
│   └── tasks.py            # Document ingestion tasks
├── workers/
│   └── ingestion.py        # Ingestion logic
├── main.py                 # App entry point
├── utils/                  # Utility scripts
└── requirements.txt

✨ Contributing

We are actively working on adding new features:

Improved document parsing for more formats

Enhanced AI summarization & extraction

Multi-document chat and better semantic search

Video & multimedia content ingestion

Contributions are welcome!

📝 License

This project is licensed under the MIT License.

❤️ Made with love by Shivansh Pareek
We will continue to add new features to make it even better.
