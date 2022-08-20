from typing import List

from app.entities.doctor import Doctor


class SqlDoctorRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, doctor: Doctor):
        self.db_session.add(doctor)

    def get(self, reference):
        return self.db_session.query(Doctor).filter_by(reference=reference).one()

    def list(self) -> List[Doctor]:
        return self.db_session.query(Doctor).all()
