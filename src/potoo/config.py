from pydantic import BaseSettings, Field

# todo: figure out how to use SecretStr with containers

class TwitterConfig(BaseSettings):
    api_key: str = Field(..., env="TWITTER_API_KEY")
    api_secret: str = Field(..., env="TWITTER_API_SECRET")
    bearer_token: str = Field(..., env="TWITTER_BEARER_TOKEN")


class DatabaseConfig(BaseSettings):
    url: str = Field(..., env="TWITTER_GROWTH_DATABASE_URL")
