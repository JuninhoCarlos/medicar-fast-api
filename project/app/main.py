import logging

from fastapi import FastAPI

from app.adapters import orm
from app.db import init_db
from app.routes import doctor, ping

log = logging.getLogger("uvicorn")
orm.start_mappers()


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(ping.router)
    application.include_router(doctor.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db()


@app.on_event("shutdown")
async def shodown_event():
    log.info("shutting down...")
