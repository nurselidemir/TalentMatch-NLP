import re
# regex kütüphanesi bir metnin içinde belirli bir desen aramak için kullanılır.
import spacy 
# NLP ile ad soyad ayrıştırmak için

def extract_email(text):
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    # pattern metinde arayacağımız yapıyı (şablonu) temsil ediyor.
    matches = re.findall(pattern, text)
    # text içinde pattern a uyan tüm eşleşmeleri liste olarak verir.
    if matches:
        return matches[0]
    return None

def extract_phone(text):
    
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{2}[-.\s]?\d{2}"
    # ? -> varsa al yoksa alma anlamına gelir.
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
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

