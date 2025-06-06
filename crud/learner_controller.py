from sqlalchemy.orm import sessionmaker
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.user import User, UserRole
from models.learner import Learner
from db.database import engine
from schemas.learner_schemas import LearnerCreate
import datetime as date


def add_learner(learner_obj: LearnerCreate, session_add_learner) -> None:
    try:
        new_user = Learner(
            name=learner_obj.name,
            firstname=learner_obj.firstname,
            email=learner_obj.email,
            birth_date=learner_obj.birth_date,
            date_create=learner_obj.date_create,
            role=learner_obj.role,
            phone=learner_obj.phone,
            platform_registration_date=learner_obj.platform_registration_date,
        )

        session_add_learner.add(new_user)
        session_add_learner.commit()

        print(f"User: {new_user.id}")
        print(f"User statut: {UserRole.learner}")
        session_add_learner.close()

    except Exception as exc:
        print("-" * 25)
        print("L'utilisateur n'a pas été ajouté")
        print(f"Exception: {exc}")
        print("-" * 25)
