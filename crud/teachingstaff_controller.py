import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.teachingstaff import TeachingStaff
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


def get_all_teachingstaff_as_create(session) -> list[TeachingStaffCreate]:
    try:
        list_result = []
        # list of all TeachingStaff in session
        teachingstaffs = session.query(TeachingStaff).all()
        # Conversion TeachingStaff -> TeachingStaffCreate
        for teachingstaff in teachingstaffs:
            create_teachingstaff = TeachingStaffCreate(**teachingstaff.model_dump())
            list_result.append(create_teachingstaff)
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la lecture de l'utilisateur")
        print(f"Exception: {exc}")
        print("-" * 25)
        return []
