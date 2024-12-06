from factory.alchemy import SQLAlchemyModelFactory

from tests.conftest import Session


def session():
    return Session


class DbModelFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session_factory = session
        sqlalchemy_session_persistence = "flush"
