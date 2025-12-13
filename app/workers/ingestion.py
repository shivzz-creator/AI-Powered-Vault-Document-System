from app.celery_app import celery_app
from app.services.extractor import extract_text
from app.services.chunker import chunk_text
from app.services.embedder import embed_texts
from app.models.db import SessionLocal, Document, DocumentChunk

@celery_app.task(name="app.workers.ingestion.ingest_document")
def ingest_document(document_id: str, file_path: str):
    db = SessionLocal()
    try:
        document = db.query(Document).filter(Document.id == document_id).first()
        document.status = "processing"
        db.commit()

        # 1️⃣ Extract text
        text = extract_text(file_path)

        # 2️⃣ Chunk text
        chunks = chunk_text(text)

        # 3️⃣ Generate embeddings
        embeddings = embed_texts([c["text"] for c in chunks])

        # 4️⃣ Store chunks + embeddings
        for chunk, embedding in zip(chunks, embeddings):
            db.add(
                DocumentChunk(
                    document_id=document_id,
                    chunk_index=chunk["index"],
                    chunk_text=chunk["text"],
                    embedding=embedding.tolist()
                )
            )

        document.status = "ready"
        db.commit()

    except Exception as e:
        document.status = "failed"
        db.commit()
        raise e

    finally:
        db.close()
