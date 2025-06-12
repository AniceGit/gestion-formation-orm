import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.inscription import Inscription
from schemas.inscription_schemas import InscriptionCreate
from sqlmodel import select

# region create


def add_inscription(
    inscription_obj: InscriptionCreate, session_add_inscription
) -> None:
    """
    Ajoute une inscription à la base de données.

    Args:
        inscription_obj (InscriptionCreate): L'objet d'inscription à ajouter.
        session_add_inscription: La session de base de données pour l'ajout.

    Raises:
        Exception: Si une erreur se produit lors de l'ajout de l'inscription.

    Returns:
        None
    """
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


# region read


def get_all_inscriptions_as_create(session) -> list[InscriptionCreate]:
    """
    Récupère toutes les inscriptions actives de la base de données.

    Args:
        session: La session de base de données pour exécuter la requête.

    Returns:
        list[InscriptionCreate]: Une liste d'objets InscriptionCreate contenant les informations des inscriptions.
    """
    try:
        statement = select(Inscription).where(Inscription.is_active == True)
        list_result = []
        # list of all Inscription in session
        inscriptions = session.exec(statement).all()
        # Conversion Inscription -> InscriptionCreate
        for inscription in inscriptions:
            create_inscription = InscriptionCreate(**inscription.model_dump())
            list_result.append(create_inscription)
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la lecture des inscriptions")
        print(f"Exception: {exc}")
        print("-" * 25)
        return []


# region delete


def delete_inscription_by_attr(attri: str, value: any, session) -> bool:
    """
    Supprime une inscription de la base de données en fonction d'un attribut et de sa valeur.

    Args:
        attri (str): L'attribut de l'inscription à filtrer.
        value (any): La valeur de l'attribut à filtrer.
        session: La session de base de données pour exécuter la requête.

    Returns:
        bool: True si l'inscription a été supprimée, False sinon."""
    try:
        inscription = (
            session.exec(select(Inscription))
            .filter(getattr(Inscription, attri) == value)
            .first()
        )
        if inscription:
            inscription_id = inscription.id
            session.delete(inscription)
            session.commit()
            print(f"Inscription supprimée : {inscription_id}")
            return True
        else:
            print(
                f"Aucune inscription trouvée avec l'attribut: {attri} ayant la valeur : {value}"
            )
            return False
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la suppression de l'inscription'")
        print(f"Exception: {exc}")
        print("-" * 25)
        return False


# region update


def update_inscription_by_attr(
    attri: str, value: any, update_data: dict, session
) -> bool:
    """
    Met à jour une inscription dans la base de données en fonction d'un attribut et de sa valeur.

    Args:
        attri (str): L'attribut de l'inscription à filtrer.
        value (any): La valeur de l'attribut à filtrer.
        update_data (dict): Un dictionnaire contenant les données à mettre à jour.
        session: La session de base de données pour exécuter la requête.

    Returns:
        bool: True si l'inscription a été mise à jour, False sinon.
    """
    try:
        inscription = (
            session.exec(select(Inscription))
            .filter(getattr(Inscription, attri) == value)
            .first()
        )
        if inscription:
            for key, val in update_data.items():
                if hasattr(inscription, key):
                    setattr(inscription, key, val)
            session.add(inscription)
            session.commit()
            print(f"Inscription mise à jour : {inscription.id}")
            return True
        else:
            print(
                f"Aucune inscription trouvée avec l'attribut: {attri} ayant la valeur : {value}"
            )
            return False
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la mise à jour de l'inscription")
        print(f"Exception: {exc}")
        print("-" * 25)
        return False
