from app.embeddings.encoder import EmbeddingEncoder
from app.retrieval.vector_search import search_similar_chunks



def build_context(question: str, top_k: int = 5):
    """
    Builds RAG context from vector search
    """
    query_embedding = EmbeddingEncoder.encode(question)

    results = search_similar_chunks(
        query_embedding=query_embedding,
        top_k=top_k
    )

    context_blocks = []
    sources = []

    for idx, item in enumerate(results):
        context_blocks.append(
            f"[Source {idx+1}]\n{item['text']}"
        )
        sources.append({
            "source_id": idx + 1,
            "document_id": item["document_id"],
            "score": item["score"]
        })

    context_text = "\n\n".join(context_blocks)

    return context_text, sources
