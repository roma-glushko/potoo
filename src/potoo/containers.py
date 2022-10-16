from dependency_injector import containers, providers
from dependency_injector.providers import Configuration, Singleton

from potoo.config import Config
from potoo.database.engine import Database
from potoo.repositories import CandidateRepository, PromoUserRepository
from potoo.services import PromoUserService, CandidateService
from potoo.services.twitter import TwitterUserService, get_twitter_client


class Runtime(containers.DeclarativeContainer):
    config: Configuration[Config] = Configuration()

    db = providers.Singleton(Database, uri=config.db.uri)
    twitter_client = providers.Singleton(
        get_twitter_client,
        api_key=config.twitter.api_key,
        api_secret=config.twitter.api_secret,
        access_token=config.twitter.access_token,
        access_token_secret=config.twitter.access_token_secret,
    )

    promo_user_repository: Singleton[PromoUserRepository] = Singleton(
        PromoUserRepository,
        session_factory=db.provided.session,
    )
    candidate_repository: Singleton[CandidateRepository] = Singleton(
        CandidateRepository,
        session_factory=db.provided.session,
    )

    twitter_user_service: Singleton[TwitterUserService] = Singleton(
        TwitterUserService,
        twitter_client=twitter_client,
    )
    promo_user_service: Singleton[PromoUserService] = Singleton(
        PromoUserService,
        promo_user_repository=promo_user_repository,
        twitter_user_service=twitter_user_service,
    )
    candidate_service: Singleton[CandidateService] = Singleton(
        CandidateService,
        candidate_repository=candidate_repository,
        twitter_user_service=twitter_user_service,
    )