from dependency_injector import containers, providers

from potoo.config import DatabaseConfig, TwitterConfig
from potoo.database.engine import Database


class Container(containers.DeclarativeContainer):
    db_config = providers.Configuration(pydantic_settings=[DatabaseConfig()])
    twitter_config = providers.Configuration(pydantic_settings=[TwitterConfig()])

    db = providers.Singleton(Database, db_url=db_config.url)