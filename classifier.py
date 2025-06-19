from transformers import pipeline
# HuggingFace kütüphanesinden pipeline fonksiyonunu alıyoruz. Bu zeki modelleri çağırmak için kullanılır.

classifier = pipeline("zero-shot-classification", model = "facebook/bart-large-mnli")
# pipeline fonksyionuna türü zero-shot-classification olan modeli facebook/bart-large-mnli olan bir sınıflandırıcı veriyoruz.
# bu sayede elimizde etiketli eğitim verisi olmasa bile, metni önceden belirlenmiş kategorilere göre sınıflandırabiliyoruz

def classify_cv_section(text, labels = None):
    if labels is None:
        labels = ["Education", "Experience", "Skills"]
    # model bu beş başlıktan hangisiyle en çok eşleştiğine karar verecek.
    result = classifier(text, candidate_labels = labels)
    return result["labels"][0]
# daha önce tanımladığımız classifier, HuggingFace’ten gelen zero-shot classification modeli.
# candidate_labels: aday etiketler.
# bu satırda model, metni bu etiketlerle karşılaştırır ve her biri için bir olasılık skoru üretir.

# etiketler listesinin ilk elemanını (en yüksek puanı alanı) döndürür.
# yani bu metin en çok hangi kategoriye ait gibi görünüyor, onu verir.