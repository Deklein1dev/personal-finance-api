from fastapi import FastAPI

from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/info", tags=["Info"])
async def get_info() -> dict[str, str]:
    return {
    "name": "Personal Finance API",
    "version": "0.1.0",
    "environment": "development",
    }
