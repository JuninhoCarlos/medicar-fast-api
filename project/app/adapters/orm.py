from sqlalchemy import Column, Integer, MetaData, String, Table, Text
from sqlalchemy.orm import mapper

from app.models.doctor import Doctor  # isort:skip

metadata = MetaData()

doctor = Table(
    "doctor",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("crm", Integer, unique=True),
    Column("email", Text),
)


def start_mappers():
    mapper(Doctor, doctor)
