from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint
from enum import Enum
from datetime import date


class UserRole(str, Enum):
    learner = "Learner"
    trainer = "Trainer"
    techingstaff = "TeachingStaff"
    admin = "Admin"


class User(SQLModel, table=False):
    """Base model for users, used as a parent class for other user types"""

    __tablename__ = "user"
    __table_args__ = (UniqueConstraint("email"),)
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)  # required field
    firstname: str = Field(max_length=50)  # required field
    email: str  # required field
    birth_date: date  # required field
    date_create: date  # required field
    is_active: bool = Field(default=True)  # required field
    role: UserRole  # required field
