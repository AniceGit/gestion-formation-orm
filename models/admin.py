from sqlmodel import Field, SQLModel, Relationship
from typing import List
from enum import Enum
import datetime as date


class AdminRole(str, Enum):
    SUPERADMIN = "SUPERADMIN"
    ADMIN_STANDARD = "ADMIN_STANDARD"
    admins: List["Admin"] = Relationship(
        back_populates="roles", link_model="AdminAdminRoleLink"
    )


class Admin(SQLModel, table=True):
    __tablename__ = "admin"
    id: int = Field(default=None, primary_key=True)
    id_user: int = Field(foreign_key="user.id")
    access_level: List[AdminRole] = Relationship(
        back_populates="admins", link_model="AdminAdminRoleLink"
    )  # required field
    promotion_date: date  # required field


class AdminAdminRoleLink(SQLModel, table=True):
    __tablename__ = "admin_adminrole_link"
    admin_id: int = Field(foreign_key="admin.id", primary_key=True)
    role_id: int = Field(foreign_key="admin_roles.id", primary_key=True)
