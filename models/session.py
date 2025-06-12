from sqlmodel import Field, SQLModel
from datetime import date
from enum import Enum
from typing import Optional, List
from sqlalchemy import Column, JSON


# enum for status in session
class StatusEnum(str, Enum):
    """Enumération pour les statuts de session"""

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    ARCHIVED = "ARCHIVED"


class Session(SQLModel, table=True):
    """Modèle pour les sessions de formation"""

    __tablename__ = "session"
    __table_args__ = {"extend_existing": True}
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: Optional[str] = None
    start_date: date
    end_date: date
    max_capacity: int
    status: StatusEnum = Field(default=StatusEnum.OPEN)
    requirements: List[str] = Field(default=None, sa_column=Column(JSON))
    id_trainer: int = Field(foreign_key="trainer.id")
    id_room: int = Field(foreign_key="room.id")
