import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from typing import Optional
from pydantic import BaseModel, Field
import datetime as date
from models.inscription import InscriptionStatusEnum


class InscriptionCreate(BaseModel):
    apprenant_id: int = Field(...)
    session_id: int = Field(...)
    statut_inscription: InscriptionStatusEnum
    presence: Optional[bool] = None

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


def main():
    info_user_dict = [
        {
            "apprenant_id": 1,
            "session_id": 101,
            "statut_inscription": InscriptionStatusEnum.ENREGISTRE,
            "presence": True
        },
        {
            "apprenant_id": 2,
            "session_id": 102,
            "statut_inscription": InscriptionStatusEnum.EN_ATTENTE,
            "presence": None
        },
        {
            "apprenant_id": 3,
            "session_id": 101,
            "statut_inscription": InscriptionStatusEnum.DESINSCRIT,
            "presence": False
        }
    ]

    new_users = [InscriptionCreate(**item) for item in info_user_dict]
    print(new_users[0].statut_inscription)
    print(new_users[0].presence)


if __name__ == "__main__":
    main()