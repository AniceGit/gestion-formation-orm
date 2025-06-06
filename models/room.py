from sqlmodel import Field, SQLModel
from typing import Dict, Any
from sqlalchemy import Column, JSON


class Room(SQLModel, table=True):
    __tablename__ = "room"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    capacity: int
    localization: str
    stuff: Dict[str, Any] = Field(default=None, sa_column=Column(JSON))
    is_active: bool = True
