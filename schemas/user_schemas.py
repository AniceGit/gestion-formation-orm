import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.user import UserRole
from typing import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints, Field
import datetime as date
from dateutil.relativedelta import relativedelta
from typing import Optional


class UserCreate(BaseModel):
    """Schema pour créer un utilisateur."""

    name: Annotated[str, StringConstraints(max_length=50)]
    firstname: Annotated[str, StringConstraints(max_length=50)]
    email: EmailStr = Field(unique=True)
    birth_date: date.date = Field(None, le=date.date.today() - relativedelta(years=16))
    date_create: date.date
    role: UserRole = UserRole.trainer

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class UserUpdate(BaseModel):
    """Schema pour mettre à jour un utilisateur."""

    name: Optional[str] = None
    firstname: Optional[str] = None
    email: EmailStr = Field(unique=True)

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
