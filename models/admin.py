from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from datetime import date
import models.user as u


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


class Admin(u.User, table=True):
    __tablename__ = "admin"
    access_level: List[AdminRole] = Relationship(
        back_populates="admins", link_model=AdminAdminRoleLink
    )  # required field
    promotion_date: date  # required field
