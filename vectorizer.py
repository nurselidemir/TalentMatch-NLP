from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text: str) -> np.ndarray:
    """
    Tek bir metni alır, embedding (vektör) olarak döner.
    """
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding

if __name__ == "__main__":
    sample = "This is a test sentence about AI and NLP."
    vec = embed_text(sample)
    print("Embedding shape:", vec.shape)
    print("First 5 values:", vec[:5])
