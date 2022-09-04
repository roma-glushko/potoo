from dependency_injector import containers, providers

from twitter_growth.config import DatabaseConfig, TwitterConfig
from twitter_growth.database.engine import Database


class Container(containers.DeclarativeContainer):
    db_config = providers.Configuration(pydantic_settings=[DatabaseConfig()])
    twitter_config = providers.Configuration(pydantic_settings=[TwitterConfig()])

    db = providers.Singleton(Database, db_url=db_config.url)