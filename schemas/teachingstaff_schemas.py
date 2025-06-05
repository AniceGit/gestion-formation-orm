import sys
import os
import datetime as date
from typing import Dict, Annotated, Any
from pydantic import BaseModel, EmailStr, StringConstraints, Field

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.teachingstaff import TeachingStaffRole
from models.user import UserRole


class TeachingStaffCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)]
    firstname: Annotated[str, StringConstraints(max_length=50)]
    email: EmailStr  # `unique=True` supprimé (non supporté ici)
    age: Annotated[int, Field(gt=16)]
    date_create: date.date
    role: UserRole = UserRole.user_techingstaff
    work: TeachingStaffRole
    date_appointement: date.date  # Correction : instancier `date.date`, pas le module
    responsabilities: Dict[str, Any]

    class Config:
        arbitrary_types_allowed = True  # Corrige l'erreur pour les types personnalisés
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


def main():
    info_user_dict = [
        {
            "name": "John",
            "firstname": "Doe",
            "email": "john.doe@generator.com",
            "age": 42,
            "date_create": date.datetime.now().date(),
            "work": "RESPONSABLE PEDAGOGIQUE",
            "date_appointement": date.datetime.now().date(),  # Correction ici
            "responsabilities": {"cours": "Python", "level": "advanced"},
        },
        {
            "name": "Jane",
            "firstname": "Doe",
            "email": "jane.doe@generator.com",
            "age": 40,
            "date_create": date.datetime.now().date(),
            "work": "CHARGEE DE PROJET",
            "date_appointement": date.datetime.now().date(),  # Correction ici
            "responsabilities": {"cours": "Java", "level": "advanced"},
        },
    ]

    new_users = [TeachingStaffCreate(**item) for item in info_user_dict]
    print(new_users[0].name)
    print(new_users[0].responsabilities)


if __name__ == "__main__":
    main()
