import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.learner import Learner
from schemas.learner_schemas import LearnerCreate

#region create

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

# region read

def get_all_learner_as_create(session) -> list[LearnerCreate]:
    try:
        list_result = []
        # list of all Learner in session
        learners = session.query(Learner).all()
        # Conversion Learner -> LearnerCreate
        for learner in learners:
            create_learner = LearnerCreate(**learner.model_dump())
            list_result.append(create_learner)
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la lecture de l'utilisateur")
        print(f"Exception: {exc}")
        print("-" * 25)
        return []
