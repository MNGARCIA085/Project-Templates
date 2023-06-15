#https://dev.to/jbrocher/fastapi-testing-a-database-5ao5

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from ..database import Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#from ..main import app, get_db
from main import app
from db.temp import get_db



SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



"""
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
"""





################################################

""" FXITURES """

import pytest

from sqlalchemy.orm import Session

from models import movies



from fastapi import FastAPI
from typing import Any, Generator


from fastapi.testclient import TestClient

def start_application():
    app = FastAPI()
    #app.include_router(router)
    return app



@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)  # Create the tables.
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)



@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[TestingSessionLocal, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session  # use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()






@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: TestingSessionLocal
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client




# add a movie to the database
@pytest.fixture(scope='function')
def add_movie(db_session: TestingSessionLocal):
    def _add_movie(title, description):

        db_movie = movies.Movie(title=title, description=description)
        db_session.add(db_movie)
        db_session.commit()
        db_session.refresh(db_movie)


        return db_movie
    return _add_movie





