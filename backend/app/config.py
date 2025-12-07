from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    debug: bool = False
    app_name: str = "Paris Gratuit API"
    version: str = "0.1.0"

    class Config:
        env_file = ".env"

settings = Settings()