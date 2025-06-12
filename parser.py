import re
# regex kütüphanesi bir metnin içinde belirli bir desen aramak için kullanılır.

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