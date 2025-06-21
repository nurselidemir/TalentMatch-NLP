from pymongo import MongoClient
import gridfs
from bson import ObjectId

def download_file_from_mongodb(file_id, output_path, mongo_uri="mongodb://localhost:27017", db_name="talentmatch"):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    fs = gridfs.GridFS(db)

    file_data = fs.get(ObjectId(file_id))  # ID ile dosyayı al
    with open(output_path, "wb") as f:
        f.write(file_data.read())  # diske yaz

    print(f"✅ File downloaded and saved as {output_path}")

# Örnek kullanım
if __name__ == "__main__":
    file_id = input(" Enter File ID: ").strip()
    output_path = input("💾 Output filename (e.g., cv_downloaded.pdf): ").strip()
    download_file_from_mongodb(file_id, output_path)
