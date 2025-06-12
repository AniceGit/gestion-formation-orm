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
    statement = select(TeachingStaff).where(TeachingStaff.is_active == True)
    results = session.exec(statement).all()
    all_learner = [TeachingStaffCreate(**item.model_dump()) for item in results]
    return all_learner


def del_teachingstaff(email: str, session):
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
