import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schemas import user_schemas as us_sche
from typing import Optional, Annotated
from pydantic import StringConstraints, Field
import datetime as date


class TrainerCreate(us_sche.UserCreate):
    speciality: str
    date_hire: date.date = Field(None, le=date.date.today())
    hourly_rate: Annotated[float, Field(ge=0.0)]
    bio: Annotated[Optional[str], StringConstraints(max_length=255)] = None

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class TrainerUpdate(us_sche.UserUpdate):
    speciality: Optional[str] = None
    hourly_rate: Optional[float] = None

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
