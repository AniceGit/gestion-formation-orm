from sqlmodel import Field, SQLModel, create_engine
from enum import Enum
from datetime import date


class UserRole(str, Enum):
    user_learner = "Learner"
    user_trainer = "Trainer"
    user_techingstaff = "TeachingStaff"
    user_admin = "Admin"


class User(SQLModel, table=True):
    __tablename__ = "user"
    id: int | None = Field(default=None, primary_key=True)
    name: str  # required field
    firstname: str  # required field
    email: str  # required field
    age: int  # required field
    date_create: date  # required field
    is_active: bool = Field(default=True)  # required field
    role: UserRole  # required field
