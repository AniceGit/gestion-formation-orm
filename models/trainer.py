from sqlmodel import Field, SQLModel
from typing import Optional
import datetime as date


class Trainer(SQLModel, table=True):
    __tablename__ = "learner"
    id: int | None = Field(default=None, primary_key=True)
    id_user: int = Field(foreign_key="User.id")
    speciality: str  # required field
    date_hire: date  # required field
    hourly_rate: float  # required field
    bio: Optional[str]  # required field
