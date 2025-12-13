from fastapi import FastAPI
from app.models.db import init_db
from app.api.v1.upload import router as upload_router

app = FastAPI(title="AI Powered Vault")

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(upload_router, prefix="/v1")

@app.get("/health")
def health_check():
    return {"status": "ok"}
