from sqlmodel import Field, SQLModel
from enum import Enum
import datetime as date


class TeachingStaffRole(str, Enum):
    EDUCATIONAL_MANAGER = "RESPONSABLE PEDAGOGIQUE"
    PROJECT_HANDLER = "CHARGEE DE PROJET"


class TeachingStaff(SQLModel, table=False):
    __tablename__ = "user"
    id: int = Field(default=None, primary_key=True)
    id_user: int = Field(foreign_key="user.id")
    work: TeachingStaffRole  # required field
    date_appointement: date  # required field
    responsabilities: str  # required field
