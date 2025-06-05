from sqlmodel import Field, SQLModel, create_engine
from datetime import date
from enum import Enum
from typing import Optional


# enum for status in session
class StatusEnum(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    ARCHIVED = "ARCHIVED"


class Session(SQLModel, table=True):
    __tablename__ = "session"
    id_session: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: Optional[str] = None
    start_date: date
    end_date: date
    max_capacity: int
    status: StatusEnum = Field(default=StatusEnum.OPEN)
    requirements: str
    id_trainer: int = Field(foreign_key="trainer.id_trainer")
    id_room: int = Field(foreign_key="room.id_room")
