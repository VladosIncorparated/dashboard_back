from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: str

    LOG_PATH:str

    APP_HOST: str
    APP_PORT: int

    @property
    def BACKEND_CORS_ORIGINS(self):
        return self.BACKEND_CORS_ORIGINS.split(",")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
