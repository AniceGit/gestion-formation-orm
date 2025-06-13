import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.trainer import Trainer
from sqlmodel import select, update
from schemas.trainer_schemas import TrainerCreate

# region create


def add_trainer(trainer_obj: TrainerCreate, session_add_trainer) -> None:
    """
    Ajoute un enseignant à la base de données.

    Args:
        trainer_obj (TrainerCreate): L'objet d'enseignant à ajouter.
        session_add_trainer: La session de base de données pour l'ajout.

    Raises:
        Exception: Si une erreur se produit lors de l'ajout de l'enseignant.

    Returns:
        None
    """
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
    """
    Récupère tous les enseignants actifs de la base de données.

    Args:
        session: La session de base de données pour exécuter la requête.

    Returns:
        list[TrainerCreate]: Une liste d'objets TrainerCreate contenant les informations des enseignants.
    """
    statement = select(Trainer).where(Trainer.is_active == True)
    results = session.exec(statement).all()
    all_learner = [TrainerCreate(**item.model_dump()) for item in results]
    return all_learner


def del_trainer(email: str, session):
    """
    Supprime un enseignant de la base de données en le marquant comme inactif.

    Args:
        email (str): L'email de l'enseignant à supprimer.
        session: La session de base de données pour exécuter la requête.

    Raises:
        ValueError: Si aucun enseignant avec l'email spécifié n'est trouvé.

    Returns:
        None
    """
    try:
        statement = (
            update(Trainer)
            .where(Trainer.email == email)
            .where(Trainer.is_active == 1)
            .values(is_active=0)
        )
        session.exec(statement)
        session.commit()
        session.close()
    except:
        raise ValueError(f"Aucun  enseignant avec l'email : {email}")


def upd_trainer(trainer_obj: Trainer, session_upd_trainer) -> None:
    """
    Met à jour les informations d'un enseignant dans la base de données.

    Args:
        trainer_obj (Trainer): L'objet d'enseignant à mettre à jour.
        session_upd_trainer: La session de base de données pour la mise à jour.

    Raises:
        ValueError: Si aucun enseignant avec l'email spécifié n'est trouvé.

    Returns:
        None
    """
    try:
        statement = (
            select(Trainer)
            .where(Trainer.email == trainer_obj.email)
            .where(Trainer.is_active == 1)
        )
        teachingstaff_info = session_upd_trainer.exec(statement).first()
        update_fields = trainer_obj.model_dump(exclude_unset=1)

        for key, value in update_fields.items():
            setattr(teachingstaff_info, key, value)

        session_upd_trainer.add(teachingstaff_info)
        session_upd_trainer.commit()
        session_upd_trainer.close()

    except:
        raise ValueError(f"Aucun apprenant avec l'email : {trainer_obj}")
