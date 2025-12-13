import os
from fastapi import UploadFile
from app.config import STORAGE_DIR

def save_file(document_id: str, file: UploadFile):
    os.makedirs(STORAGE_DIR, exist_ok=True)
    file_path = os.path.join(STORAGE_DIR, f"{document_id}_{file.filename}")

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path
