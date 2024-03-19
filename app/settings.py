from pydantic import SecretStr
from pydantic_settings import BaseSettings

__all__ = ['settings']


class Settings(BaseSettings):
    debug: bool
    iris_bot_shortname: str
    iris_channel_shortname: str

    api_id: SecretStr
    api_secret: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
