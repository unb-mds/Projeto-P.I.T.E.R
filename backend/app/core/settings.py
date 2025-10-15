from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "PITER API"
    APP_VERSION: str = "0.1.0"
    CORS_ORIGINS: str = "http://localhost:3000"

    class Config:
        env_file = ".env"

settings = Settings()
