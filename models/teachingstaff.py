from sqlmodel import Field, SQLModel, create_engine
from sqlalchemy import Column, JSON
from typing import Optional, Any, Dict
from enum import Enum
from datetime import date


class TeachingStaffRole(str, Enum):
    EDUCATIONAL_MANAGER = "RESPONSABLE PEDAGOGIQUE"
    PROJECT_HANDLER = "CHARGEE DE PROJET"


class TeachingStaff(SQLModel, table=True):
    __tablename__ = "teaching_staff"
    id: int = Field(default=None, primary_key=True)
    id_user: int = Field(foreign_key="user.id")
    work: TeachingStaffRole  # required field
    date_appointement: date  # required field
    responsabilities: Optional[Dict[str, Any]] = Field(
        default=None, sa_column=Column(JSON)
    )
