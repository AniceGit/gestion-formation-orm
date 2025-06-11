import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.admin import Admin, AdminRole, AdminAdminRoleLink
from db.database import engine
from schemas.admin_schemas import AdminCreate, AdminRoleCreate, AdminAdminRoleLinkCreate
from sqlmodel import select


def add_admin(admin_obj: AdminCreate, session_add_admin) -> None:
    # try:
    #     new_user = Admin(admin_obj.model_dump())

    #     session_add_admin.add(new_user)
    #     session_add_admin.commit()
    #     session_add_admin.refresh(new_user)

    #     for access_id in admin_obj.access_level:
    #         link = AdminAdminRoleLink(admin_id=new_user.id, role_id=access_id)
    #         session_add_admin.add(link)

    #     session_add_admin.commit()
    #     print(f"User: {new_user.id}")
    #     print(f"User statut: {new_user.role}")
    #     session_add_admin.close()

    # except Exception as exc:
    #     print("-" * 25)
    #     print("L'utilisateur n'a pas été ajouté")
    #     print(f"Exception: {exc}")
    #     print("-" * 25)
    new_user = Admin(**admin_obj.model_dump())

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


def find_adminrole(session) -> dict[int, str]:
    results = session.exec(select(AdminRole)).all()
    return {role.id: role.name for role in results}


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
