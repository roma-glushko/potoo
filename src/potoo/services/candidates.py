from potoo.repositories import CandidateRepository
from potoo.services.twitter import TwitterUserService


class CandidateService:
    def __init__(
        self,
        candidate_repository: CandidateRepository,
        twitter_user_service: TwitterUserService,
    ) -> None:
        self._candidate_repository: CandidateRepository = candidate_repository

        self._twitter_user_service: TwitterUserService = twitter_user_service

    def add_seed_users(self, promo_username: str, seed_usernames: list[str]) -> None:
        ...
