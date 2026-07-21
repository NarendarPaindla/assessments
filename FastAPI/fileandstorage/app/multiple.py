from pathlib import Path
from typing import Annotated
import shutil
import uuid

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
    status,
)

router = APIRouter(
    prefix="/multiplefiles",
    tags=["multiple"]
)

UPLOAD_DIR = Path("app/uploads/images")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".pdf",
}

ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/png",
    "application/pdf",
}

MAX_FILE_SIZE = 5 * 1024 * 1024


def validate_file(file: UploadFile, size: int):
    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{file.filename}: Unsupported file extension."
        )

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{file.filename}: Invalid content type."
        )

    if size == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{file.filename}: Empty files are not allowed."
        )

    if size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"{file.filename}: Maximum file size is 5 MB."
        )


@router.post("/single")
async def upload_single_file(
    file: Annotated[UploadFile, File()]
):
    content = await file.read()

    validate_file(file, len(content))

    await file.seek(0)

    extension = Path(file.filename).suffix.lower()

    filename = f"{uuid.uuid4()}{extension}"

    destination = UPLOAD_DIR / filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    await file.close()

    return {
        "message": "File uploaded successfully",
        "original_filename": file.filename,
        "stored_filename": filename,
        "content_type": file.content_type,
        "size": len(content),
        "path": str(destination)
    }


@router.post("/multiple")
async def upload_multiple_files(
    files: Annotated[list[UploadFile], File()]
):
    uploaded_files = []

    for file in files:

        content = await file.read()

        validate_file(file, len(content))

        await file.seek(0)

        extension = Path(file.filename).suffix.lower()

        filename = f"{uuid.uuid4()}{extension}"

        destination = UPLOAD_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        await file.close()

        uploaded_files.append(
            {
                "original_filename": file.filename,
                "stored_filename": filename,
                "content_type": file.content_type,
                "size": len(content),
                "path": str(destination)
            }
        )

    return {
        "message": "All files uploaded successfully",
        "total_files": len(uploaded_files),
        "files": uploaded_files
    }