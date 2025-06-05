from sqlmodel import Field, SQLModel, Relationship, create_engine
from typing import List, Optional
from enum import Enum
from datetime import date


class AdminAdminRoleLink(SQLModel, table=True):
    __tablename__ = "admin_adminrole_link"
    admin_id: int = Field(foreign_key="admin.id", primary_key=True)
    role_id: int = Field(foreign_key="admin_role.id", primary_key=True)


class AdminRole(SQLModel, table=True):
    __tablename__ = "admin_role"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # e.g. "SUPERADMIN", "ADMIN_STANDARD"
    admins: List["Admin"] = Relationship(
        back_populates="access_level", link_model=AdminAdminRoleLink
    )


class Admin(SQLModel, table=True):
    __tablename__ = "admin"
    id: int = Field(default=None, primary_key=True)
    id_user: int = Field(foreign_key="user.id")
    access_level: List[AdminRole] = Relationship(
        back_populates="admins", link_model=AdminAdminRoleLink
    )  # required field
    promotion_date: date  # required field
