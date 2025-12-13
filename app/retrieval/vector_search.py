from sqlalchemy import text
from app.db.session import engine


def search_similar_chunks(query_embedding, top_k: int = 5):
    """
    Performs cosine similarity search using pgvector
    """
    embedding_str = "[" + ",".join(map(str, query_embedding)) + "]"

    sql = text("""
        SELECT
            document_id,
            chunk_text,
            1 - (embedding <=> :embedding) AS similarity
        FROM document_chunks
        ORDER BY embedding <=> :embedding
        LIMIT :top_k;
    """)

    with engine.connect() as conn:
        results = conn.execute(
            sql,
            {"embedding": embedding_str, "top_k": top_k}
        ).fetchall()

    return [
        {
            "document_id": row[0],
            "text": row[1],
            "score": float(row[2])
        }
        for row in results
    ]
