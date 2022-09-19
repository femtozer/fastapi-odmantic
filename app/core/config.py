import logging

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = "local"
    LOG_LEVEL: int = logging.INFO
    API_PREFIX: str = "/api"
    MONGO_CONNECTION_STRING: str

    class Config:
        env_file = ".env"


settings = Settings()
