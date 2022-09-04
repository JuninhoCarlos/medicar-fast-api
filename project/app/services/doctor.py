from app.models import Especialidade
from app.repositories import BaseRepository


def create_speciality(
    especialiadade: Especialidade, specialityRepository: BaseRepository
):
    specialityRepository.save(especialiadade)


def get_all_specialities(specialityRepository: BaseRepository):
    return specialityRepository.list()
