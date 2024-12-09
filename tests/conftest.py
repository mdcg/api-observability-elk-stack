import pytest
from starlette.testclient import TestClient

from task_service.application.api import app
from task_service.infrastructure.database import connection
from task_service.infrastructure.database.connection import SessionLocal

Session = SessionLocal()


@pytest.fixture(scope="function", autouse=True)
def session():
    db = Session
    try:
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture(scope="function")
def client(session):
    def override_session():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[connection.session] = override_session
    yield TestClient(app)
