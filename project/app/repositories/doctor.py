from sqlalchemy import select

from app.models.doctor import Especialidade


class BaseRepository:
    def save(self):
        pass

    def get(self):
        pass

    def list(self):
        pass


class SqlSpecialityRepository(BaseRepository):
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, doctor: Especialidade):
        self.db_session.add(doctor)

    def get(self, reference):
        return self.db_session.query(Speciality).filter_by(reference=reference).one()

    def list(self) -> list[Especialidade]:
        query = select(Especialidade)
        return self.db_session.execute(query).all()
