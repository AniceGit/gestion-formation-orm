import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.learner import Learner
from sqlmodel import select
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


# region read


def get_learner(session) -> LearnerCreate:
    results = session.exec(select(Learner)).all()
    all_learner = [LearnerCreate(**item.model_dump()) for item in results]
    return all_learner


# region delete


def delete_learner_by_attr(attri: str, value: any, session) -> bool:
    try:
        learner = (
            session.exec(select(Learner))
            .filter(getattr(Learner, attri) == value)
            .first()
        )
        if learner:
            learner_name = learner.name
            session.delete(learner)
            session.commit()
            print(f"Apprenant supprimé : {learner_name}")
            return True
        else:
            print(
                f"Aucun apprenant trouvé avec l'attribut: {attri} ayant la valeur : {value}"
            )
            return False
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la suppression de l'apprenant'")
        print(f"Exception: {exc}")
        print("-" * 25)
        return False
