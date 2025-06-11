import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.inscription import Inscription
from schemas.inscription_schemas import InscriptionCreate

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
        inscriptions = session.query(Inscription).all()
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
            session.query(Inscription)
            .filter(getattr(Inscription, attri) == value)
            .first()
        )
        if inscription:
            inscription_name = inscription.name
            session.delete(inscription)
            session.commit()
            print(f"Salle supprimée : {inscription_name}")
            return True
        else:
            print(
                f"Aucune salle trouvée avec l'attribut: {attri} et la valeur : {value}"
            )
            return False
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la suppression de la salle")
        print(f"Exception: {exc}")
        print("-" * 25)
        return False
