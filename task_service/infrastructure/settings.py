from pydantic_settings import BaseSettings, SettingsConfigDict
from os import environ

class Settings(BaseSettings):
    DATABASE_USER: str = environ.get("DATABASE_USER")
    DATABASE_PASSWORD: str = environ.get("DATABASE_PASSWORD")
    DATABASE_NAME: str = environ.get("DATABASE_NAME")
    DATABASE_HOST: str = environ.get("DATABASE_HOST")
    DATABASE_PORT: str = environ.get("DATABASE_PORT")

settings = Settings()
