import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.teachingstaff import TeachingStaff
from sqlmodel import select
from schemas.teachingstaff_schemas import TeachingStaffCreate

# region create


def add_teachingstaff(
    teachingstaff_obj: TeachingStaffCreate, session_add_teachingstaff
) -> None:
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
    results = session.exec(select(TeachingStaff)).all()
    all_teachingstaff = [TeachingStaffCreate(**item.model_dump()) for item in results]
    return all_teachingstaff


# region delete


def delete_teachingstaff_by_attr(attri: str, value: any, session) -> bool:
    try:
        teachingstaff = (
            session.exec(select(TeachingStaff))
            .filter(getattr(TeachingStaff, attri) == value)
            .first()
        )
        if teachingstaff:
            teachingstaff_name = teachingstaff.name
            session.delete(teachingstaff)
            session.commit()
            print(f"Staff pédago supprimé : {teachingstaff_name}")
            return True
        else:
            print(
                f"Aucun staff pédago trouvé avec l'attribut: {attri} ayant la valeur : {value}"
            )
            return False
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la suppression du staff pédago")
        print(f"Exception: {exc}")
        print("-" * 25)
        return False
