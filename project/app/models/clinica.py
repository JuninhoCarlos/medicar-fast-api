from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Doctor(Base):
    __tablename__ = "doctor"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    crm = Column(Integer, unique=True)
    email = Column(Text)

    def __repr__(self):
        return f"Doctor(id={self.id!r}, name={self.name!r}, crm={self.crm!r})"
