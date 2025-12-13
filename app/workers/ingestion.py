from app.celery_app import celery_app
from app.services.extractor import extract_text
from app.models.db import SessionLocal, Document

@celery_app.task(name="app.workers.ingestion.ingest_document")
def ingest_document(document_id: str, file_path: str):
    db = SessionLocal()
    try:
        doc = db.query(Document).filter(Document.id == document_id).first()
        doc.status = "processing"
        db.commit()

        text = extract_text(file_path)

        text_path = file_path.replace(".pdf", ".txt")
        with open(text_path, "w") as f:
            f.write(text)

        doc.status = "ready"
        db.commit()

    except Exception:
        doc.status = "failed"
        db.commit()
        raise
    finally:
        db.close()
