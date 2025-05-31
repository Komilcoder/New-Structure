import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Business Trip App"
    DEBUG: bool = True
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()