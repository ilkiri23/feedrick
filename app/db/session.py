from contextlib import contextmanager
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.libs.ext.sqlalchemy import Base


engine = create_engine('sqlite:///db.sqlite' ,echo=True)
__factory = sessionmaker(engine, autoflush=False, expire_on_commit=False)


import app.db.__all_models
Base.metadata.create_all(engine)


@contextmanager
def transaction_session() -> Generator[Session, None, None]:
    with __factory() as session, session.begin():
        yield session


def create_session() -> Session:
    return __factory()


@contextmanager
def session_scope() -> Generator[Session]:
    with create_session() as session, session.begin():
        yield session


@contextmanager
def auto_commit() -> Generator[Session]:
    with create_session() as session, session.begin():
        yield session
