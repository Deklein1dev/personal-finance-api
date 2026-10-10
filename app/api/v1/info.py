from fastapi import APIRouter

from app.core.config import get_settings


router = APIRouter(
    prefix="/info",
    tags=["Information"],
)


@router.get("")
async def get_info() -> dict[str, str]:
    settings = get_settings()

    return {
        "name": settings.APP_NAME,
        "description": settings.APP_DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
