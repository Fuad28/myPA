import os
import secrets
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    TITLE: str = "MyPA"
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = secrets.token_urlsafe(32)
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_IN_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_IN_DAYS: int = 7
    DATABASE_URL: str = "sqlite://./db.sqlite3"
    CORS_ORIGINS: list[str] = [
        "http://localhost",
        "http://localhost:3000"
    ]
    CLOUDINARY_NAME: str = ""
    CLOUDINARY_API_KEY: str = ""
    CLOUDINARY_API_SECRET: str = ""
    DEFAULT_PROFILE_PIC: str = ""

    SENDGRID_API_KEY: str= os.getenv("SENDGRID_API_KEY")
    EMAIL_HOST_SENDGRID: str = os.getenv("EMAIL_HOST_SENDGRID")

    CELERY_BROKER_URL: str="redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str="redis://localhost:6379/1"


    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()