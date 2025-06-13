from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint
from typing import Optional
from datetime import date
import models.user as u


class AdminAdminRoleLink(SQLModel, table=True):
    """Table pour lier les administrateurs aux rôles"""

    __tablename__ = "admin_adminrole_link"
    __table_args__ = {"extend_existing": True}
    admin_id: int = Field(foreign_key="admin.id", primary_key=True)
    role_id: int = Field(foreign_key="admin_role.id", primary_key=True)


class AdminRole(SQLModel, table=True):
    """Table pour les rôles d'administrateur"""

    __tablename__ = "admin_role"
    __table_args__ = (UniqueConstraint("name"), {"extend_existing": True})
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # e.g. "SUPERADMIN", "ADMIN_STANDARD"


class Admin(u.User, table=True):
    """Modèle pour les administrateurs, hérite de User"""

    __tablename__ = "admin"
    __table_args__ = {"extend_existing": True}
    promotion_date: date  # required field
