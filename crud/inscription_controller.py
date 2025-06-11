import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.inscription import Inscription
from schemas.inscription_schemas import InscriptionCreate


def add_inscription(
    inscription_obj: InscriptionCreate, session_add_inscription
) -> None:
    try:
        new_inscription = Inscription(**inscription_obj.model_dump())

        session_add_inscription.add(new_inscription)
        session_add_inscription.commit()

        print(f"Inscription: {new_inscription.id}")
        session_add_inscription.close()

    except Exception as exc:
        print("-" * 25)
        print("L'inscription n'a pas été ajoutée")
        print(f"Exception: {exc}")
        print("-" * 25)
