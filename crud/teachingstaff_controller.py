import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.teachingstaff import TeachingStaff
from sqlmodel import select, update
from schemas.teachingstaff_schemas import TeachingStaffCreate

# region create


def add_teachingstaff(
    teachingstaff_obj: TeachingStaffCreate, session_add_teachingstaff
) -> None:
    """
    Ajoute un membre du personnel pédagogique à la base de données.

    Args:
        teachingstaff_obj (TeachingStaffCreate): L'objet de personnel pédagogique à ajouter.
        session_add_teachingstaff: La session de base de données pour l'ajout.

    Raises:
        Exception: Si une erreur se produit lors de l'ajout du personnel pédagogique.

    Returns:
        None
    """
    try:
        new_user = TeachingStaff(**teachingstaff_obj.model_dump())

        session_add_teachingstaff.add(new_user)
        session_add_teachingstaff.commit()

        print(f"User: {new_user.id}")
        print(f"User statut: {new_user.role}")
        session_add_teachingstaff.close()

    except Exception as exc:
        print("-" * 25)
        print("L'utilisateur n'a pas été ajouté")
        print(f"Exception: {exc}")
        print("-" * 25)


# region read


def get_teachingstaff(session) -> TeachingStaffCreate:
    """
    Récupère tous les membres du personnel pédagogique actifs de la base de données.

    Args:
        session: La session de base de données pour exécuter la requête.

    Returns:
        list[TeachingStaffCreate]: Une liste d'objets TeachingStaffCreate contenant les informations des membres du personnel pédagogique.
    """
    statement = select(TeachingStaff).where(TeachingStaff.is_active == True)
    results = session.exec(statement).all()
    all_learner = [TeachingStaffCreate(**item.model_dump()) for item in results]
    return all_learner


def del_teachingstaff(email: str, session):
    """
    Supprime un membre du personnel pédagogique de la base de données en le marquant comme inactif.

    Args:
        email (str): L'email du membre du personnel pédagogique à supprimer.
        session: La session de base de données pour exécuter la requête.

    Raises:
        ValueError: Si aucun membre du personnel pédagogique avec l'email spécifié n'est trouvé.

    Returns:
        None
    """
    try:
        statement = (
            update(TeachingStaff)
            .where(TeachingStaff.email == email)
            .where(TeachingStaff.is_active == 1)
            .values(is_active=0)
        )
        session.exec(statement)
        session.commit()
        session.close()
    except:
        raise ValueError(f"Aucun staff pédagogique avec l'email : {email}")


def upd_teachingstaff(
    teachingstaff_obj: TeachingStaff, session_upd_teachingstaff
) -> None:
    """
    Met à jour les informations d'un membre du personnel pédagogique dans la base de données.

    Args:
        teachingstaff_obj (TeachingStaff): L'objet de personnel pédagogique à mettre à jour.
        session_upd_teachingstaff: La session de base de données pour la mise à jour.

    Raises:
        ValueError: Si aucun membre du personnel pédagogique avec l'email spécifié n'est trouvé.

    Returns:
        None
    """
    try:
        statement = (
            select(TeachingStaff)
            .where(TeachingStaff.email == teachingstaff_obj.email)
            .where(TeachingStaff.is_active == 1)
        )
        teachingstaff_info = session_upd_teachingstaff.exec(statement).first()
        update_fields = teachingstaff_obj.model_dump(exclude_unset=1)

        for key, value in update_fields.items():
            setattr(teachingstaff_info, key, value)

        session_upd_teachingstaff.add(teachingstaff_info)
        session_upd_teachingstaff.commit()
        session_upd_teachingstaff.close()

    except:
        raise ValueError(f"Aucun apprenant avec l'email : {teachingstaff_obj}")
