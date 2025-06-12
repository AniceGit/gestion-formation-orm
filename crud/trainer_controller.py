import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.trainer import Trainer
from sqlmodel import select, update
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


def get_trainer(session) -> TrainerCreate:
    statement = select(Trainer).where(Trainer.is_active == True)
    results = session.exec(statement).all()
    all_learner = [TrainerCreate(**item.model_dump()) for item in results]
    return all_learner


def del_trainer(email: str, session):
    try:
        statement = (
            update(Trainer)
            .where(Trainer.email == email)
            .where(Trainer.is_active == True)
            .values(is_active=False)
        )
        session.exec(statement)
    except:
        raise ValueError(f"Aucun  enseignant avec l'email : {email}")


def upd_trainer(trainer_obj: Trainer, session_upd_trainer) -> None:
    try:
        statement = (
            select(Trainer)
            .where(Trainer.email == trainer_obj.email)
            .where(Trainer.is_active == True)
        )
        teachingstaff_info = session_upd_trainer.exec(statement).first()
        update_fields = trainer_obj.model_dump(exclude_unset=True)

        for key, value in update_fields.items():
            setattr(teachingstaff_info, key, value)

        session_upd_trainer.add(teachingstaff_info)
        session_upd_trainer.commit()
        session_upd_trainer.close()

    except:
        raise ValueError(f"Aucun apprenant avec l'email : {trainer_obj}")
