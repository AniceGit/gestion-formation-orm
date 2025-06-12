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
    try:
        list_result = []
        # list of all Inscription in session
        inscriptions = session.exec(select(Inscription)).all()
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
