import logging

from pydantic import BaseSettings, Field


class TwitterConfig(BaseSettings):
    api_key: str = Field(..., env="POTOO__TWITTER_API_KEY")
    api_secret: str = Field(..., env="POTOO__TWITTER_API_SECRET")
    access_token: str = Field(..., env="POTOO__TWITTER_ACCESS_TOKEN")
    access_token_secret: str = Field(..., env="POTOO__TWITTER_ACCESS_TOKEN_SECRET")


class DatabaseConfig(BaseSettings):
    uri: str = Field(..., env="POTOO__DATABASE_URI")


class Config(BaseSettings):
    log_level: str = Field(logging.INFO, env="POTOO__LOG_LEVEL")

    db: DatabaseConfig = Field(default_factory=DatabaseConfig)
    twitter: TwitterConfig = Field(default_factory=TwitterConfig)
