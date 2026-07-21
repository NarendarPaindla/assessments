from fastapi import (APIRouter,File,HTTPException,UploadFile,status)
from pathlib import Path
from typing import Annotated
import uuid
import shutil
router=APIRouter(prefix="/validation",tags=["File Upload"])

UPLOAD_DIR=Path("app/uploads/images")
UPLOAD_DIR.mkdir(parents=True,exist_ok=True)

ALLOWED_EXTENSIONS={
    ".jpg",
    ".jpeg",
    ".png",
    ".pdf",
    ".txt",
}

ALLOWED_CONTENT_TYPES={
    "image/jpeg",
    "image/png",
    "application/pdf",
    "text/plain",
}

MAX_FILE_SIZE=5*1024*1024

@router.post("/single")
async def upload_valide(file:Annotated[UploadFile,File()]):
    extension=Path(file.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="unsupported file extension"
        )
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid content type"
        )
    content = await file.read()
    file_size=len(content)
    if file_size==0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Empty files are not allowed"
            
        )
    if file_size>MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum alloed file size is 5MB"
    )
    await file.seek(0)

    filename=f"{uuid.uuid4()}{extension}"
    destination=UPLOAD_DIR / filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    await file.close()

    return {
        "message": "File uploaded successfully",
        "original_filename": file.filename,
        "stored_filename": filename,
        "content_type": file.content_type,
        "size": file_size,
        "path": str(destination),
    }