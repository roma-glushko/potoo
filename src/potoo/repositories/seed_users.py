from potoo.database.typing import SessionFactory


class SeedUserRepository:
    def __init__(self, session_factory: SessionFactory) -> None:
        self.session_factory = session_factory

    def add(
        self,
    ):
        ...
