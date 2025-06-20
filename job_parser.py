import re

def extract_job_title(text):
    match = re.search(r"(?i)^.*(?:Position|Title)[:\-]\s*(.*)", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def extract_required_skills(text):
    match = re.search(r"(Skills|Technologies)[:\-]\s*(.+)", text, re.IGNORECASE)
    if match:
        skills = match.group(2).split(",")
        return [s.strip() for s in skills]
    return []

def extract_experience(text):
    pattern = r"(\d+\+?\s+years of experience.*?)"
    return re.findall(pattern, text, re.IGNORECASE)

def parse_job_posting(text):
    return {
        "title": extract_job_title(text),
        "skills": extract_required_skills(text),
        "experience": extract_experience(text),
        "raw_text": text.strip()
    }



