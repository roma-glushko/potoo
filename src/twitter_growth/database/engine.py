from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, scoped_session

BaseModel = declarative_base()


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, connect_args={"check_same_thread": False})

        self.session_factory = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine
            )
        )

    def create_database(self) -> None:
        BaseModel.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Session:
        session: Session = self.session_factory()
        try:
            yield session
        except Exception as e:
            print('Session rollback because of exception: %s', e)
            session.rollback()
        finally:
            session.close()