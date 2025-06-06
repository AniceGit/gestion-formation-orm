import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.user import UserRole
from typing import Optional, Annotated, List
from pydantic import BaseModel, EmailStr, constr, StringConstraints, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
import datetime as date
from dateutil.relativedelta import relativedelta


class AdminAdminRoleLinkCreate(BaseModel):
    admin_id: int = Field(...)
    role_id: int = Field(...)

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class AdminRoleCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)]

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class AdminCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)]
    firstname: Annotated[str, StringConstraints(max_length=50)]
    email: EmailStr = Field(unique=True)
    birth_date: date.date = Field(None, ge=date.date.today() - relativedelta(years=16))
    date_create: date.date
    role: UserRole = UserRole.admin
    access_level: List[int]
    promotion_date: date.date

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
