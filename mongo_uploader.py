from pymongo import MongoClient
import gridfs

def upload_file_to_mongodb(file_path, mongo_uri="mongodb://localhost:27017", db_name="talentmatch"):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    fs = gridfs.GridFS(db)

    with open(file_path, "rb") as f:
        file_id = fs.put(f, filename=file_path.split("/")[-1])
    
    print(f"✅ File uploaded to MongoDB. ID: {file_id}")
    return file_id

# Example usage
if __name__ == "__main__":
    file_path = input("📂 Enter file path (.pdf or .docx): ").strip()
    upload_file_to_mongodb(file_path)
