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


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db












