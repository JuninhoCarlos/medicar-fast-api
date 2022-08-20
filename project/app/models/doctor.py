from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Doctor:
    id: int
    name: str
    crm: int
    email: str
