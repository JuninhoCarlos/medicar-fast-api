import os

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def init_db():
    return create_engine(os.environ.get("DATABASE_URL"))


def get_session(engine=Depends(init_db)):
    return sessionmaker(bind=engine)()
