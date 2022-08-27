from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mealsapp import config
from mealsapp.db import Base, get_db
from main import app


SQLALCHEMY_DATABASE_URL = f"postgresql://{config.DATABASE_USERNAME}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}/{config.TEST_DATABASE_NAME}"
# create an in-memory db for unit testing
# engine = create_engine("sqlite+pysqlite:///:memory:?cache=shared", echo=True, future=False, connect_args={'check_same_thread': False})

# Connect to a local POSTGRES database
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
