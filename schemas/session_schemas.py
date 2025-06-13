from pydantic import BaseModel, model_validator
from typing import Optional, List
from datetime import date
from enum import Enum


class StatusEnum(str, Enum):
    """Enumération pour les statuts des sessions"""

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    ARCHIVED = "ARCHIVED"


class SessionCreate(BaseModel):
    """Modèle pour la création d'une session de formation"""

    title: str
    description: Optional[str] = None
    start_date: date
    end_date: date
    max_capacity: int
    status: StatusEnum = StatusEnum.OPEN
    requirements: List[str]
    id_trainer: int
    id_room: int

    @model_validator(mode="after")
    def check_dates(self):
        if self.end_date <= self.start_date:
            raise ValueError("end_date must be after start_date")
        return self

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
