from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import pytest
import sys

sys.path.append("../license_provider")
from src.database import Base


@pytest.fixture
def db():
    db_name = uuid4()
    DATABASE_URL = f"sqlite:///./{db_name}.db"

    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
        os.remove(f"{db_name}.db")
