from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "sample_app"
    APP_VERSION: str = "0.0.1"
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="allow"
    )


settings = Settings()
