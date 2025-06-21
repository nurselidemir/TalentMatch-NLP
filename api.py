from fastapi import FastAPI, UploadFile, File, Form
from job_parser import parse_job_posting
from vectorizer import embed_text
from emailer import send_match_email
from parser import extract_text_from_pdf, extract_text_from_docx
import faiss
import numpy as np
import os
from dotenv import load_dotenv

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TalentMatch API is live!"}

@app.post("/match")
async def match_cvs(
    job_text: str = Form(...),
    to_email: str = Form(...),
    top_k: int = Form(2),
    cv_file: UploadFile = File(...)
):
    # Dosya uzantısına göre içeriği oku
    filename = cv_file.filename.lower()
    contents = await cv_file.read()

    if filename.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(contents)
        extracted_text = extract_text_from_pdf("temp.pdf")

    elif filename.endswith(".docx"):
        with open("temp.docx", "wb") as f:
            f.write(contents)
        extracted_text = extract_text_from_docx("temp.docx")

    else:
        return {"error": "Only .pdf and .docx files are supported."}

    # İş ilanı analizi ve embedding
    job_info = parse_job_posting(job_text)
    job_vector = embed_text(job_text)
    cv_vector = embed_text(extracted_text)

    index = faiss.IndexFlatL2(job_vector.shape[0])
    index.add(np.array([cv_vector]))
    distances, indices = index.search(np.array([job_vector]), k=top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        similarity = 100 / (1 + distances[0][i])
        similarity = float(similarity)
        cv_text_lower = extracted_text.lower()

        skills = job_info.get("skills") or []
        missing_skills = [s for s in skills if s.lower() not in cv_text_lower]

        results.append({
            "cv": extracted_text,
            "similarity": round(similarity, 2),
            "missing_skills": missing_skills
        })

    # E-posta gönderimi
    load_dotenv()
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    send_match_email(
        to_email=to_email,
        match_results=results,
        sender_email=sender_email,
        sender_password=sender_password
    )

    return {"matches": results}
