from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.config.settings import Settings, get_settings
from app.db import get_session
from app.models.doctor import Doctor

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }


@router.get("/medicos")
def medicos(db_session=Depends(get_session)):

    query = select(Doctor)
    res = db_session.execute(query).all()
    print(res)

    return {"status": "ok"}
