from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint
from typing import Optional
from datetime import date
import models.user as u


class AdminAdminRoleLink(SQLModel, table=True):
    __tablename__ = "admin_adminrole_link"
    admin_id: int = Field(foreign_key="admin.id", primary_key=True)
    role_id: int = Field(foreign_key="admin_role.id", primary_key=True)


class AdminRole(SQLModel, table=True):
    __tablename__ = "admin_role"
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # e.g. "SUPERADMIN", "ADMIN_STANDARD"


class Admin(u.User, table=True):
    __tablename__ = "admin"
    promotion_date: date  # required field
