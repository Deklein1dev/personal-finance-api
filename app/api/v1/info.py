from fastapi import APIRouter

from app.api.dependencies import SettingsDep


router = APIRouter(
    prefix="/info",
    tags=["Information"],
)


@router.get("")
async def get_info(settings: SettingsDep) -> dict[str, str]:
    return {
        "name": settings.APP_NAME,
        "description": settings.APP_DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
