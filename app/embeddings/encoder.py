from sentence_transformers import SentenceTransformer

# Lightweight + fast + high quality
MODEL_NAME = "all-MiniLM-L6-v2"

class EmbeddingEncoder:
    _model = None

    @classmethod
    def load_model(cls):
        if cls._model is None:
            cls._model = SentenceTransformer(MODEL_NAME)
        return cls._model

    @classmethod
    def encode(cls, text: str):
        model = cls.load_model()
        embedding = model.encode(text, normalize_embeddings=True)
        return embedding.tolist()
