from dependency_injector import containers, providers
from dependency_injector.providers import Configuration, Factory

from potoo.config import Config
from potoo.database.engine import Database
from potoo.repositories import PromoUserRepository


class Container(containers.DeclarativeContainer):
    config: Configuration[Config] = Configuration()

    db = providers.Singleton(Database, uri=config.db.uri)

    promo_user_repository: Factory[PromoUserRepository] = Factory(
        PromoUserRepository,
        session_factory=db.provided.session,
    )
