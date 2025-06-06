import sys
import os
import datetime as date
from typing import Dict, Annotated, Any
from pydantic import BaseModel, EmailStr, StringConstraints, Field

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.teachingstaff import TeachingStaffRole
from models.user import UserRole
from dateutil.relativedelta import relativedelta


class TeachingStaffCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)]
    firstname: Annotated[str, StringConstraints(max_length=50)]
    email: EmailStr  # `unique=True` supprimé (non supporté ici)
    birth_date: date.date = Field(None, ge=date.date.today() - relativedelta(years=16))
    date_create: date.date
    role: UserRole = UserRole.techingstaff
    work: TeachingStaffRole
    date_appointement: date.date  # Correction : instancier `date.date`, pas le module
    responsabilities: Dict[str, Any]

    class Config:
        arbitrary_types_allowed = True  # Corrige l'erreur pour les types personnalisés
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
