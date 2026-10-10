from fastapi import FastAPI

app = FastAPI(
    title="Personal Finance API",
    description="REST API for personal finance management",
    version="0.1.0",
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
