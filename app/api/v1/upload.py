from fastapi import APIRouter, UploadFile, File
import uuid
from app.services.storage import save_file
from app.models.db import SessionLocal, Document

router = APIRouter()

@router.post("/upload")
def upload_document(file: UploadFile = File(...)):
    document_id = str(uuid.uuid4())

    save_file(document_id, file)

    db = SessionLocal()
    doc = Document(
        id=document_id,
        filename=file.filename,
        status="uploaded"
    )
    db.add(doc)
    db.commit()

    return {
        "document_id": document_id,
        "filename": file.filename,
        "status": "uploaded"
    }
