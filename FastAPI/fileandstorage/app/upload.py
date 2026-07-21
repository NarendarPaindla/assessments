from fastapi import APIRouter,UploadFile,File
from typing import Annotated

router=APIRouter(prefix="/upload",tags=["File Uploads"])
file: UploadFile=File(...)

@router.post("/single")
async def upload_single_file(file:Annotated[UploadFile,File()]):
    content=await file.read()
    return {
        "filename":file.filename,
        "content-type":file.content_type,
        "size":len(content)
        }