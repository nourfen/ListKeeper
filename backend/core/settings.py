from typing import ClassVar
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"

    DEV_FRONTEND_ORIGINS: ClassVar[list[str]] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]
    
    DOCKER_FRONTEND_ORIGINS: ClassVar[list[str]] = [
        "http://localhost:8080 ",
        "http://127.0.0.1:8080",
    ]

    PROD_FRONTEND_ORIGINS: ClassVar[list[str]] = [
        "",
    ]

    @property
    def FRONTEND_ORIGINS(self) -> list[str]:
        if self.ENV == "prod":
            return self.PROD_FRONTEND_ORIGINS
        return self.DEV_FRONTEND_ORIGINS

    class Config:
        env_file = ".env"

settings = Settings()