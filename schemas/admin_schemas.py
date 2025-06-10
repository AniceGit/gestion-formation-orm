import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schemas import user_schemas as us_sche
from typing import Annotated, List
from pydantic import BaseModel, StringConstraints, Field
import datetime as date


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


class AdminCreate(us_sche.UserCreate):
    access_level: List[AdminRoleCreate]
    promotion_date: date.date

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
