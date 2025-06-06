from sqlmodel import Field, SQLModel, create_engine
from enum import Enum
from datetime import date


class UserRole(str, Enum):
    user_learner = "Learner"
    user_trainer = "Trainer"
    user_techingstaff = "TeachingStaff"
    user_admin = "Admin"


class User(SQLModel, table=False):
    __tablename__ = "user"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)  # required field
    firstname: str = Field(max_length=50)  # required field
    email: str  # required field
    birth_date: date  # required field
    date_create: date  # required field
    is_active: bool = Field(default=True)  # required field
    role: UserRole  # required field
