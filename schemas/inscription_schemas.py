from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


# enum for inscription_status in session
class InscriptionStatusEnum(str, Enum):
    ENREGISTRE = "ENREGISTRE"
    DESINSCRIT = "DESINSCRIT"
    EN_ATTENTE = "EN_ATTENTE"


class InscriptionCreate(BaseModel):
    inscription_date: datetime
    inscription_status: InscriptionStatusEnum
    presence: Optional[bool] = None
    id_session: int
    id_learner: int

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
