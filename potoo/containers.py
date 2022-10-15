from dependency_injector import containers, providers
from dependency_injector.providers import Configuration

from potoo.config import Config
from potoo.database.engine import Database


class Container(containers.DeclarativeContainer):
    config: Configuration[Config] = Configuration()

    db = providers.Singleton(Database, uri=config.db.uri)
