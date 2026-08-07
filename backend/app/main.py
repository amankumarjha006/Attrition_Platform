from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import get_settings
from app.core.logger import logger

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Employee Attrition API...")

    # Future:
    # Load model
    # Load preprocessor
    # Load SHAP explainer

    logger.info("Startup completed.")

    yield

    logger.info("Shutting down Employee Attrition API...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)


@app.get("/", tags=["Root"])
async def root():
    logger.info("Root endpoint called")

    return {
        "message": f"{settings.APP_NAME} is running.",
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG,
    }