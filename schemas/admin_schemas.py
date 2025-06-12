import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schemas import user_schemas as us_sche
from typing import Annotated, List
from pydantic import BaseModel, StringConstraints, Field
import datetime as date


class AdminAdminRoleLinkCreate(BaseModel):
    """Schema pour créer une liaison entre un administrateur et un rôle."""

    admin_id: int = Field(...)
    role_id: int = Field(...)

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class AdminRoleCreate(BaseModel):
    """Schema pour créer un rôle d'administrateur."""

    name: Annotated[str, StringConstraints(max_length=50)]

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class AdminCreate(us_sche.UserCreate):
    """Schema pour créer un administrateur."""

    access_level: List[int]  # list of AdminRole:id
    promotion_date: date.date

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class AdminUpdate(us_sche.UserUpdate):
    """Schema pour mettre à jour un administrateur."""

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
