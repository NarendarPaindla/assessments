from pathlib import Path

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)

from app.services.storage_service import LocalStorageService

router = APIRouter(
    prefix="/storage",
    tags=["storage"],
)

ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
}

MAX_FILE_SIZE = 5 * 1024 * 1024


@router.post("/profile")
async def upload_profile_image(
    file: UploadFile = File(...),
):
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only JPEG, PNG and WEBP images are allowed.",
        )

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="Maximum allowed size is 5 MB.",
        )

    file.file.seek(0)

    saved = LocalStorageService.save_file(
        file=file,
        category="profiles",
    )

    return {
        "message": "Profile uploaded successfully.",
        "data": saved,
    }


@router.post("/resume")
async def upload_resume(
    file: UploadFile = File(...),
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Resume must be a PDF.",
        )

    saved = LocalStorageService.save_file(
        file=file,
        category="resumes",
    )

    return {
        "message": "Resume uploaded successfully.",
        "data": saved,
    }


@router.post("/certificate")
async def upload_certificate(
    file: UploadFile = File(...),
):
    saved = LocalStorageService.save_file(
        file=file,
        category="certificates",
    )

    return {
        "message": "Certificate uploaded successfully.",
        "data": saved,
    }


@router.post("/assignment")
async def upload_assignment(
    file: UploadFile = File(...),
):
    saved = LocalStorageService.save_file(
        file=file,
        category="assignments",
    )

    return {
        "message": "Assignment uploaded successfully.",
        "data": saved,
    }


@router.post("/course-thumbnail")
async def upload_course_thumbnail(
    file: UploadFile = File(...),
):
    saved = LocalStorageService.save_file(
        file=file,
        category="course_thumbnails",
    )

    return {
        "message": "Thumbnail uploaded successfully.",
        "data": saved,
    }
