from sqlalchemy import (
    create_engine,
    Column,
    String,
    DateTime,
    Integer,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
from app.config import DATABASE_URL

from pgvector.sqlalchemy import Vector

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True)
    filename = Column(String, nullable=False)
    status = Column(String, default="uploaded")
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    chunks = relationship("DocumentChunk", back_populates="document")


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, ForeignKey("documents.id"))
    chunk_index = Column(Integer)
    chunk_text = Column(Text)

    embedding = Column(Vector(384))  # sentence-transformers dimension

    document = relationship("Document", back_populates="chunks")


def init_db():
    Base.metadata.create_all(bind=engine)
