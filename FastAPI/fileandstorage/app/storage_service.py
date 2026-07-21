from pathlib import Path
import shutil
import uuid

from fastapi import UploadFile


class LocalStorageService:
    """
    Handles all local file storage operations.

    Future:
        Replace this implementation with
        AWS S3
        Azure Blob
        Google Cloud Storage

    without changing API routes.
    """

    BASE_DIR = Path("app/uploads")

    @classmethod
    def save_file(
        cls,
        file: UploadFile,
        category: str,
    ):
        extension = Path(file.filename).suffix.lower()

        directory = cls.BASE_DIR / category

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = f"{uuid.uuid4()}{extension}"

        destination = directory / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {
            "filename": filename,
            "category": category,
            "path": destination,
            "url": f"/uploads/{category}/{filename}",
        }