import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schemas import user_schemas as us_sche
from typing import Optional
from pydantic import Field
from pydantic_extra_types.phone_numbers import PhoneNumber
import datetime as date


class LearnerCreate(us_sche.UserCreate):
    study_level: Optional[str] = None  # unrequired field
    phone: Optional[PhoneNumber] = None  # unrequired field
    platform_registration_date: date.date = Field(default=date.datetime.now())

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
