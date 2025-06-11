import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.trainer import Trainer
from schemas.trainer_schemas import TrainerCreate


def add_trainer(trainer_obj: TrainerCreate, session_add_trainer) -> None:
    try:
        new_user = Trainer(**trainer_obj.model_dump())

        session_add_trainer.add(new_user)
        session_add_trainer.commit()

        print(f"User: {new_user.id}")
        print(f"User statut: {new_user.role}")
        session_add_trainer.close()

    except Exception as exc:
        print("-" * 25)
        print("L'utilisateur n'a pas été ajouté")
        print(f"Exception: {exc}")
        print("-" * 25)
