import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.teachingstaff import TeachingStaff
from db.database import engine
from schemas.teachingstaff_schemas import TeachingStaffCreate


def add_teachingstaff(
    teachingstaff_obj: TeachingStaffCreate, session_add_teachingstaff
) -> None:
    try:
        new_user = TeachingStaff(
            name=teachingstaff_obj.name,
            firstname=teachingstaff_obj.firstname,
            email=teachingstaff_obj.email,
            birth_date=teachingstaff_obj.birth_date,
            date_create=teachingstaff_obj.date_create,
            role=teachingstaff_obj.role,
            work=teachingstaff_obj.work,
            date_appointement=teachingstaff_obj.date_appointement,
            responsabilities=teachingstaff_obj.responsabilities,
        )

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
