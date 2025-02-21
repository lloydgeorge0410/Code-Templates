from pydantic_settings import BaseSettings, SettingsConfigDict

from app.utils.constants import MODE


class Settings(BaseSettings):
    port: int = 5000
    host: str = "127.0.0.1"
    mode: str = MODE.DEV

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
