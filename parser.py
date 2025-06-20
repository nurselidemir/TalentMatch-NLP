import re
# regex kütüphanesi bir metnin içinde belirli bir desen aramak için kullanılır.
import spacy 
# NLP ile ad soyad ayrıştırmak için
import re

def extract_email(text):
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    # pattern metinde arayacağımız yapıyı (şablonu) temsil ediyor.
    matches = re.findall(pattern, text)
    # text içinde pattern a uyan tüm eşleşmeleri liste olarak verir.
    if matches:
        return matches[0]
    return None

def extract_phone(text):
    """
    +90 532 747 4000 veya +44 7911 123456 gibi numaraları tam olarak yakalar.
    """
    pattern = r"(\+?\d[\d\s\-().]{9,})"
    match = re.search(pattern, text)
    if match:
        phone = match.group().strip()
        digits = re.sub(r"\D", "", phone)
        if len(digits) >= 10:
            return phone
    return None


nlp = spacy.load("en_core_web_sm")
# spacynin ingilizce dil modelini yükledik.
# nlp değişkeni artık bir metni işleyecek hazır dil işlemcisi oldu.

def extract_name(text):

    doc = nlp(text)  # doc artık işlenmis spaCy belgesi(analiz edilmiş metin)
    for ent in doc.ents:   # doc.ents spacynin buldugu tüm entity(varlıkları)döner.
        if ent.label_ == "PERSON":
            return ent.text
    return None 

def extract_sections_from_labeled(labeled_sections):
    """
    HuggingFace ile etiketlenmiş metinleri temiz ve sabit anahtarlarla döndürür.
    """
    parsed = {
        "education": labeled_sections.get("Education", []),
        "experience": labeled_sections.get("Experience", []),
        "skills": labeled_sections.get("Skills", [])
    }
    return parsed
