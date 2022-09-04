from fastapi import APIRouter, Depends

from app import services
from app.db import get_session
from app.repositories import SqlSpecialityRepository

router = APIRouter()


@router.get("/especialidades")
def medicos(db_session=Depends(get_session)):
    repository = SqlSpecialityRepository(db_session)
    specialities = services.get_all_specialities(repository)

    return [speciality.Speciality for speciality in specialities]
