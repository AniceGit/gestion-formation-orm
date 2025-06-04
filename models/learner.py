from sqlmodel import Field, SQLModel, create_engine
from typing import Optional
from enum import Enum
import datetime as date


class Learner(SQLModel, table=True):
    __tablename__ = "learner"
    id: int | None = Field(default=None, primary_key=True)
    id_user: int = Field(foreign_key="User.id")
    birth_date: date  # required field
    study_level: Optional[str]  # unrequired field
    phone: Optional[str]  # unrequired field
    platform_registration_date: date  # required field
