from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    FILE_SAVE_PATH: str


    class Config:
        env_file = ".env"
