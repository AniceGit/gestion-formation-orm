import datetime as date
from typing import Dict, Any, Optional
from pydantic import Field

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.teachingstaff import TeachingStaffRole
from schemas import user_schemas as us_sche


class TeachingStaffCreate(us_sche.UserCreate):
    """Schema pour créer un membre du personnel enseignant."""
    work: TeachingStaffRole
    date_appointement: date.date = Field(None, le=date.date.today())
    responsabilities: Optional[Dict[str, Any]]

    class Config:
        arbitrary_types_allowed = True
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class TeachingStaffUpdate(us_sche.UserUpdate):
    """Schema pour mettre à jour un membre du personnel enseignant."""
    work: Optional[TeachingStaffRole] = None

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
