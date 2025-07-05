from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "✅ File uploaded successfully", "filename": file.filename}
