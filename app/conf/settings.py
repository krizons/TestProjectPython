from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    FILE_SAVE_PATH: str
    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str
    LOGIN: str
    PASS: str
    IMAGE_SAVE_PATH: str
    class Config:
        env_file = ".env"
