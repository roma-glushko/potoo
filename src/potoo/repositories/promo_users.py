from potoo.database import PromoUser
from potoo.database.typing import SessionFactory


class PromoUserRepository:
    def __init__(self, session_factory: SessionFactory) -> None:
        self.session_factory = session_factory

    def add(self, user_id: str) -> PromoUser:
        with self.session_factory() as session:
            user = PromoUser(user_id=user_id)

            session.add(user)
            session.commit()
            session.refresh(user)

            return user
