from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from job_parser import parse_job_posting
from vectorizer import embed_text
import faiss
import numpy as np
from emailer import send_match_email
import os
from dotenv import load_dotenv


# FastAPI uygulamasını başlat
app = FastAPI()

# Basit root endpoint
@app.get("/")
def home():
    return {"message": "TalentMatch API is live!"}

# İstek verisi için model
class MatchRequest(BaseModel):
    job_text: str
    cv_texts: List[str]
    top_k: int = 2  # admin isterse değiştirebilir.
    to_email: str  # eşleşme sonucu nereye gitsin?

# CV eşleştirme endpoint'i
@app.post("/match")
def match_cvs(data: MatchRequest):
    job_info = parse_job_posting(data.job_text)
    job_vector = embed_text(data.job_text)
    cv_vectors = np.array([embed_text(cv) for cv in data.cv_texts])

    index = faiss.IndexFlatL2(job_vector.shape[0])
    index.add(cv_vectors)
    distances, indices = index.search(np.array([job_vector]), k=data.top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        similarity = 100 / (1 + distances[0][i])
        similarity = float(similarity)  
        cv_text = data.cv_texts[idx]
        cv_text_lower = cv_text.lower()

        skills = job_info.get("skills") or []
        missing_skills = [s for s in skills if s.lower() not in cv_text_lower]

        results.append({
            "cv": cv_text,
            "similarity": round(similarity, 2),
            "missing_skills": missing_skills
        })

    # 📨 E-posta ile gönderim
    load_dotenv()
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    send_match_email(
        to_email=data.to_email,
        match_results=results,
        sender_email=sender_email,
        sender_password=sender_password
    )

    return {"matches": results}
