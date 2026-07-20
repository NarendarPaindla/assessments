from fastapi import APIRouter, Request

from app.core.limiter import limiter

router = APIRouter()


@router.get("/courses")
@limiter.limit("10/minute")
async def get_courses(request: Request):
    return {
        "courses": [
            "Python",
            "FastAPI",
            "React"
        ]
    }