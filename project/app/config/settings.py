import logging
import os

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", None)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


async def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
