from sqlmodel import Field, SQLModel
from enum import Enum
import datetime as date


class UserRole(str, Enum):
    user_learner = "Learner"
    user_trainer = "Trainer"
    user_techingstaff = "TeachingStaff"
    user_admin = "Admin"


class User(SQLModel, table=False):
    __tablename__ = "user"
    id: int | None = Field(default=None, primary_key=True)
    name: str  # required field
    firstname: str  # required field
    email: str  # required field
    age: int  # required field
    date_create: date  # required field
    is_active: bool = Field(default=True)  # required field
    role: UserRole  # required field
