from pypdf import PdfReader
# pypdf kütüphanesinden PdfReader adında bir sınıf (araç) alıyoruz. Bu araç .pdf uzantılı dosyaları açıp içindeki metni çıkarabiliyor.
from docx import Document
import os
# Python’ın dosya işlemleri için sunduğu yerleşik bir kütüphane. Dosyanın uzantısını .pdf mi .docx mi ayırmak için kullanıyoruz.
from parser import extract_email, extract_phone, extract_name

def extract_text_from_pdf(pdf_path):  # pdften metin çıkarma fonksiyonu
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:    # reader içindeki sayfaları tek tek dolaşıyoruz
        text += page.extract_text() # extract_text() metodu, o sayfadan düz metni (text) çıkarır.
    return text
# extract_text(): pypdf kütüphanesindeki PageObject sınıfının metodudur.
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

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
