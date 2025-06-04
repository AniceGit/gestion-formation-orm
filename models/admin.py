from sqlmodel import Field, SQLModel, create_engine
from enum import Enum
import datetime as date


class AdminRole(str, Enum):
    SUPERADMIN = "SUPERADMIN"
    ADMIN_STANDARD = "ADMIN_STANDARD"


class Admin(SQLModel, table=True):
    __tablename__ = "admin"
    id: int | None = Field(default=None, primary_key=True)
    id_user: int = Field(foreign_key="User.id")
    access_level: list[AdminRole]  # required field
    promotion_date: date  # required field


class AdminAdminRoleLink(SQLModel, table=True):
    admin_id: int = Field(foreign_key="admin.id", primary_key=True)
    role_id: int = Field(foreign_key="adminrole.id", primary_key=True)
