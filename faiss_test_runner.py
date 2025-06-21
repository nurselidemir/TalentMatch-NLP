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
    score = 1 / (1 + distances[i])
    percent = round(score * 100, 2)
    print(f"{i+1}. CV {idx} → {cv_texts[idx]}")
    print(f"   Similarity: {percent}% (distance: {distances[i]:.4f})")

def find_missing_skills(job_skills, cv_skills):
    """
    İş ilanındaki becerilerden, CV'de eksik olanları döner.
    Karşılaştırma büyük/küçük harfe duyarsızdır.
    """
    job_skills_set = {s.lower().strip() for s in job_skills}
    cv_skills_set = {s.lower().strip() for s in cv_skills}

    missing = job_skills_set - cv_skills_set
    return list(missing)

job_skills = ["Python", "FastAPI", "Docker", "TensorFlow"]
cv_skills = ["Python", "FastAPI", "Pandas"]

missing = find_missing_skills(job_skills, cv_skills)
print("\nMissing Skills:", missing)