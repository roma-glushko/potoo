from pydantic import BaseSettings, Field


class TwitterConfig(BaseSettings):
    api_key: str = Field(..., env="POTOO__TWITTER_API_KEY")
    api_secret: str = Field(..., env="POTOO__TWITTER_API_SECRET")
    bearer_token: str = Field(..., env="POTOO__TWITTER_BEARER_TOKEN")


class DatabaseConfig(BaseSettings):
    uri: str = Field(..., env="POTOO__DATABASE_URI")


class Config(BaseSettings):
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)
    twitter: TwitterConfig = Field(default_factory=TwitterConfig)
