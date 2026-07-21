from pathlib import Path
from typing import Annotated
import shutil
import uuid

from fastapi import APIRouter,File,UploadFile

router=APIRouter(prefix="/local",tags=["local storage"])
UPLOAD_DIR=Path("app/uploads/images")
UPLOAD_DIR.mkdir(parents=True,exist_ok=True)
@router.post("/upload")
async def upload_local(file:Annotated[UploadFile,File()]):
    extension=Path(file.filename).suffix
    filename=f"{uuid.uuid4()}{extension}"
    destination=UPLOAD_DIR / filename
    with  destination.open("wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    await file.close()

    return {
        "message":"File uploaded successfully",
        "original_filename":file.filename,
        "stored_filename":filename,
        "content-type":file.content_type,
        "path":str(destination)
    }
