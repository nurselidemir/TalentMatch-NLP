import os
# Python’ın dosya işlemleri için sunduğu yerleşik bir kütüphane. Dosyanın uzantısını .pdf mi .docx mi ayırmak için kullanıyoruz.
from parser import extract_email, extract_phone, extract_name
from sectioner import segment_and_classify_sections
from parser import extract_sections_from_labeled
from parser import summarize_text
from parser import extract_text_from_pdf, extract_text_from_docx


if __name__ == "__main__":
    file_name = input("📂 Lütfen .pdf veya .docx dosyasının yolunu girin: ").strip()
    # .strip() -> ifadenin başında ve sonundaki boşlukları ve gizli karakterleri (örn. \n, \t) temizler.
    extension = os.path.splitext(file_name)[1].lower()
    # os.path.splitext -> dosya adını ve uzantısını ayırır. 2.elemanı yani uzantıyı alır.
    if extension == ".pdf":
        extracted_text = extract_text_from_pdf(file_name)
    elif extension == ".docx":
        extracted_text = extract_text_from_docx(file_name)
    else:
        raise ValueError("❌ Sadece .pdf veya .docx dosyaları destekleniyor.")

    print("\n📄 Dosyadan çıkarılan metin:")
    print(extracted_text[:500])

    print("📧 E-posta adresi:", extract_email(extracted_text))
    print("📞 Telefon numarası:", extract_phone(extracted_text))
    print("🧑 Ad Soyad:", extract_name(extracted_text))
    
sections = segment_and_classify_sections(extracted_text)

for label, paras in sections.items():
    print(f"\n{label.upper()}")
    for p in paras:
        print(f" - {p}")

parsed = extract_sections_from_labeled(sections)

print("\n Structured Output:")
print("Education:", parsed["education"])
print("Experience:", parsed["experience"])
print("Skills:", parsed["skills"])


summary = summarize_text(extracted_text)
print("\n CV summary:")
print(summary)
    