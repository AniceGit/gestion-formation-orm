from sqlmodel import Field, SQLModel
from datetime import datetime
from enum import Enum
from typing import Optional


# enum for inscription_status in session
class InscriptionStatusEnum(str, Enum):
    ENREGISTRE = "ENREGISTRE"
    DESINSCRIT = "DESINSCRIT"
    EN_ATTENTE = "EN_ATTENTE"


class Inscription(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    inscription_date: datetime = Field(default=datetime.now())
    inscription_status: InscriptionStatusEnum
    presence: Optional[bool]
    id_session: int = Field(foreign_key="session.id")
    id_learner: int = Field(foreign_key="learner.id")
