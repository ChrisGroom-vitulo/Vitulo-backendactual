
from fastapi import APIRouter, UploadFile

router = APIRouter()

@router.post("/")
def upload_file(file: UploadFile):
    return {"filename": file.filename, "status": "uploaded"}
