from fastapi import FastAPI

from app.api.health.router import router as health_router
from app.api.v1.router import api_router
from app.core.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.include_router(health_router)

app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX,
)
