from pydantic import BaseSettings, Field


class BaseConfig(BaseSettings):
    class Config:
        env_prefix = "POTOO__"


class TwitterConfig(BaseConfig):
    api_key: str = Field(..., env="TWITTER_API_KEY")
    api_secret: str = Field(..., env="TWITTER_API_SECRET")
    bearer_token: str = Field(..., env="TWITTER_BEARER_TOKEN")


class DatabaseConfig(BaseConfig):
    uri: str = Field(..., env="DATABASE_URI")
