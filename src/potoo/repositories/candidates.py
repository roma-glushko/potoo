from potoo.database import SeedUser
from potoo.database.typing import SessionFactory


class CandidateRepository:
    """ """

    def __init__(self, session_factory: SessionFactory) -> None:
        self.session_factory = session_factory

    def add_seed_users(
        self,
        promo_user_id: str,
        seed_users: list[str],
    ) -> None:
        with self.session_factory() as session:
            for user_id in seed_users:
                seed_user = SeedUser(promo_user_id=promo_user_id, user_id=user_id)
                session.add(seed_user)

            session.commit()
