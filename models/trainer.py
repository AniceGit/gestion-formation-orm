from sqlmodel import Field, SQLModel, create_engine
from typing import Optional
from datetime import date
import models.user as u


class Trainer(u.User, table=True):
    __tablename__ = "trainer"
    speciality: str  # required field
    date_hire: date  # required field
    hourly_rate: float  # required field
    bio: Optional[str]  # required field
