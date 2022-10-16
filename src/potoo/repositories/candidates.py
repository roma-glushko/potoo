from potoo.database import SeedUser
from potoo.database.typing import SessionFactory


class CandidateRepository:
    """ """

    def __init__(self, session_factory: SessionFactory) -> None:
        self.session_factory = session_factory

    def add_seed_users(
        self,
        promo_username: str,
        seed_usernames: list[str],
    ) -> None:
        with self.session_factory() as session:
            for username in seed_usernames:
                seed_user = SeedUser(promo_username=promo_username, user_id=user_id)
                session.add(seed_user)

            session.commit()
