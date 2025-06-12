import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.trainer import Trainer
from sqlmodel import select
from schemas.trainer_schemas import TrainerCreate

# region create


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


# region read


def get_trainer(session) -> TrainerCreate:
    results = session.exec(select(Trainer)).all()
    all_learner = [TrainerCreate(**item.model_dump()) for item in results]
    return all_learner


# region delete


def delete_trainer_by_attr(attri: str, value: any, session, is_active=True) -> bool:
    try:
        trainer = (
            session.exec(select(Trainer))
            .filter(getattr(Trainer, attri) == value)
            .first()
        )
        if trainer:
            if is_active:
                trainer.is_active = False
                session.add(trainer)
                session.commit()
                print(f"Formateur désactivé : {trainer.name}")
                return True
            else:
                trainer_name = trainer.name
                session.delete(trainer)
                session.commit()
                print(f"Formateur supprimé : {trainer_name}")
                return True
        else:
            print(
                f"Aucune formateur trouvée avec l'attribut: {attri} ayant la valeur : {value}"
            )
            return False
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la suppression du formateur")
        print(f"Exception: {exc}")
        print("-" * 25)
        return False
