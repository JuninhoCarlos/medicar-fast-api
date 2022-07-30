import os
from sqlalchemy import create_engine


def init_db():
    return create_engine(os.environ.get("DATABASE_URL"))
