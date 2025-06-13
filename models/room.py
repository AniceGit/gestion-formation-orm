from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint
from typing import Dict, Any
from sqlalchemy import Column, JSON


class Room(SQLModel, table=True):
    """Modèle pour les salles de formation"""

    __tablename__ = "room"
    __table_args__ = (UniqueConstraint("name"), {"extend_existing": True})
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    capacity: int
    localization: str
    stuff: Dict[str, Any] = Field(default=None, sa_column=Column(JSON))
    is_active: bool = True
