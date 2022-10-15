from potoo.database import PromoUser
from potoo.database.typing import SessionFactory


class PromoUserRepository:
    def __init__(self, session_factory: SessionFactory) -> None:
        self.session_factory = session_factory

    def add(self, username: str) -> PromoUser:
        with self.session_factory() as session:
            user = PromoUser(username=username)

            session.add(user)
            session.commit()
            session.refresh(user)

            return user
