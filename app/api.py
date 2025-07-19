from fastapi import APIRouter, UploadFile, File
from app.services import process_document

router = APIRouter()

@router.post("/extract")
async def extract_document(file: UploadFile = File(...)):
    result = await process_document(file)
    return result