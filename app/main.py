from fastapi import FastAPI
from app.models.db import init_db
from app.api.v1.upload import router as upload_router
from app.api import chat  # chat.py with /chat endpoints

# Create one FastAPI app object
app = FastAPI(title="AI Powered Vault Document System")

# Include routers
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(upload_router, prefix="/v1", tags=["Upload"])

# Startup event to initialize DB
@app.on_event("startup")
def startup_event():
    init_db()

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
