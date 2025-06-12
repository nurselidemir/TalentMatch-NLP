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
