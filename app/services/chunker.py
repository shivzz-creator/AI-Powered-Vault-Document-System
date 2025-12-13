def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50):
    """
    Splits text into overlapping chunks.
    """
    words = text.split()
    chunks = []

    start = 0
    index = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)

        chunks.append({
            "index": index,
            "text": chunk_text
        })

        index += 1
        start += chunk_size - overlap

    return chunks
