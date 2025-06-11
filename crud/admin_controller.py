import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.admin import Admin, AdminRole, AdminAdminRoleLink
from schemas.admin_schemas import AdminCreate, AdminRoleCreate, AdminAdminRoleLinkCreate
from sqlmodel import select


def add_admin(admin_obj: AdminCreate, session_add_admin) -> None:
    try:
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

    except Exception as exc:
        print("-" * 25)
        print("L'utilisateur n'a pas été ajouté")
        print(f"Exception: {exc}")
        print("-" * 25)


def get_admin(session) -> AdminCreate:
    results = session.exec(select(Admin)).all()
    all_link = get_admin_adminrole_link(session)

    all_admin = []
    for item in results:
        admin_data = item.model_dump()
        roles = [link.role_id for link in all_link if link.admin_id == item.id]
        admin_data["access_level"] = roles
        admin = AdminCreate(**admin_data)
        all_admin.append(admin)
    return all_admin


def get_adminrole(session) -> dict[int, str]:
    results = session.exec(select(AdminRole)).all()
    return {role.id: role.name for role in results}


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


def get_admin_adminrole_link(session) -> AdminAdminRoleLinkCreate:
    results = session.exec(select(AdminAdminRoleLink)).all()
    all_link = [AdminAdminRoleLinkCreate(**item.model_dump()) for item in results]
    return all_link
