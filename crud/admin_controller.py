import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.admin import Admin, AdminRole, AdminAdminRoleLink
from db.database import engine
from schemas.admin_schemas import AdminCreate, AdminRoleCreate, AdminAdminRoleLinkCreate


def add_admin(admin_obj: AdminCreate, session_add_admin) -> None:
    try:
        new_user = Admin(
            name=admin_obj.name,
            firstname=admin_obj.firstname,
            email=admin_obj.email,
            birth_date=admin_obj.birth_date,
            date_create=admin_obj.date_create,
            role=admin_obj.role,
            promotion_date=admin_obj.promotion_date,
        )

        session_add_admin.add(new_user)
        session_add_admin.commit()
        session_add_admin.refresh(new_user)

        for access_id in admin_obj.access_level:
            link = AdminAdminRoleLink(admin_id=new_user.id, role_id=access_id)
            session_add_admin.add(link)

        session_add_admin.commit()
        print(f"User: {new_user.id}")
        print(f"User statut: {new_user.role}")
        session_add_admin.close()

    except Exception as exc:
        print("-" * 25)
        print("L'utilisateur n'a pas été ajouté")
        print(f"Exception: {exc}")
        print("-" * 25)


# TODO Objectif : trouver les id de chaque role de la list access_level
def find_admin_role(admin_obj: AdminCreate, session_add_admin) -> None:
    pass


# TODO Objectif : trouver l'id de l'admin créé
def find_admin_id(admin_obj: AdminCreate, session_add_admin) -> None:
    pass


def add_admin_role(admin_obj: AdminRoleCreate, session_add_admin_role) -> None:
    try:
        new_admin_role = AdminRole(
            name=admin_obj.name,
        )

        session_add_admin_role.add(new_admin_role)
        session_add_admin_role.commit()

        print(f"Role: {new_admin_role.id}")
        session_add_admin_role.close()

    except Exception as exc:
        print("-" * 25)
        print("Le role n'a pas été ajouté")
        print(f"Exception: {exc}")
        print("-" * 25)
