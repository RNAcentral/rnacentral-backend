from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_driver: str = "postgresql"
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    @property
    def db_uri(self) -> str:
        return f"{self.db_driver}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file="../.env")


@lru_cache
def get_settings():
    return Settings()
