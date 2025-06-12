import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.learner import Learner
from sqlmodel import select, update
from schemas.learner_schemas import LearnerCreate

# region create


def add_learner(learner_obj: LearnerCreate, session_add_learner) -> None:
    try:
        new_user = Learner(**learner_obj.model_dump())

        session_add_learner.add(new_user)
        session_add_learner.commit()

        print(f"User: {new_user.id}")
        print(f"User statut: {new_user.role}")
        session_add_learner.close()

    except Exception as exc:
        print("-" * 25)
        print("L'utilisateur n'a pas été ajouté")
        print(f"Exception: {exc}")
        print("-" * 25)


def get_learner(session) -> LearnerCreate:
    statement = select(Learner).where(Learner.is_active == True)
    results = session.exec(statement).all()
    all_learner = [LearnerCreate(**item.model_dump()) for item in results]
    return all_learner


def del_learner(email: str, session):
    try:
        statement = (
            update(Learner)
            .where(Learner.email == email)
            .where(Learner.is_active == True)
            .values(is_active=False)
        )
        session.exec(statement)
    except:
        raise ValueError(f"Aucun apprenant avec l'email : {email}")


def upd_learner(learner_obj: LearnerCreate, session_upd_learner) -> None:
    try:
        statement = (
            select(Learner)
            .where(Learner.email == learner_obj.email)
            .where(Learner.is_active == True)
        )
        learner_info = session_upd_learner.exec(statement).first()
        update_fields = learner_obj.model_dump(exclude_unset=True)

        for key, value in update_fields.items():
            setattr(learner_info, key, value)

        session_upd_learner.add(learner_info)
        session_upd_learner.commit()
        session_upd_learner.close()

    except:
        raise ValueError(f"Aucun apprenant avec l'email : {learner_obj}")
