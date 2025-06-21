import faiss
import numpy as np

def build_faiss_index(embedding_list):
    """
    Liste halinde gelen vektör embedding'lerinden FAISS index oluşturur.
    """
    dimension = embedding_list[0].shape[0]  
    index = faiss.IndexFlatL2(dimension)   
    index.add(np.array(embedding_list).astype('float32'))
    return index

def search_similar(query_embedding, index, top_k=5):
    """
    Verilen sorgu embedding'iyle en benzer top_k sonucu döndürür.
    """
    query_vector = np.array([query_embedding]).astype('float32')
    distances, indices = index.search(query_vector, top_k)
    return distances[0], indices[0]
