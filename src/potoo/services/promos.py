from potoo.database import PromoUser
from potoo.repositories import PromoUserRepository
from potoo.services.twitter import TwitterUserService


class PromoUserService:
    """ """

    def __init__(
        self,
        promo_user_repository: PromoUserRepository,
        twitter_user_service: TwitterUserService,
    ) -> None:
        self._promo_user_repository: PromoUserRepository = promo_user_repository

        self._twitter_user_service = twitter_user_service

    def add_promo_user(self, username: str) -> PromoUser:
        profile = self._twitter_user_service.fetch_profile_by_username(username)

        return self._promo_user_repository.add(
            user_id=profile.id_str,
            username=username,
        )
