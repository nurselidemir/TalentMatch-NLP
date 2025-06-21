from vectorizer import embed_text
from faiss_indexer import build_faiss_index, search_similar

cv_texts = [
    "Experienced data scientist skilled in Python, SQL, and machine learning.",
    "Backend developer with knowledge of FastAPI, Docker, and databases.",
    "AI researcher with focus on NLP, HuggingFace Transformers, and deep learning."
]

job_text = "We are looking for a machine learning engineer with strong skills in Python and data analysis."

cv_embeddings = [embed_text(text) for text in cv_texts]
job_embedding = embed_text(job_text)


index = build_faiss_index(cv_embeddings)

distances, indices = search_similar(job_embedding, index, top_k=2)

print("\nTop matching CVs:")
for i, idx in enumerate(indices):
    print(f"{i+1}. CV {idx} → {cv_texts[idx]}")
    print(f"   Distance (lower = more similar): {distances[i]:.4f}")
