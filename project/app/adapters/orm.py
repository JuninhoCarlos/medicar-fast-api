from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table, Text
from sqlalchemy.orm import mapper, relationship

from app import models

metadata = MetaData()

speciality_table = Table(
    "especialidade",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nome", String(50)),
)

doctor_table = Table(
    "doctor",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("crm", Integer, unique=True),
    Column("email", Text),
    Column("speciality_id", Integer, ForeignKey("especialidade.id")),
)


def start_mappers():
    mapper(
        models.Especialidade,
        speciality_table,
    )

    mapper(
        models.Doctor,
        doctor_table,
        properties={"especialidade": relationship(models.Especialidade)},
    )
