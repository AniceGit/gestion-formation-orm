from sqlmodel import Field, SQLModel, create_engine
from typing import Optional
from datetime import date


class Trainer(SQLModel, table=True):
    __tablename__ = "trainer"
    id: int | None = Field(default=None, primary_key=True)
    id_user: int = Field(foreign_key="user.id")
    speciality: str  # required field
    date_hire: date  # required field
    hourly_rate: float  # required field
    bio: Optional[str]  # required field
