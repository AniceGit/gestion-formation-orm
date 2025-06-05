from sqlmodel import Field, Session, SQLModel, create_engine
from typing import Dict, Any
from sqlalchemy import Column, JSON


class Room(SQLModel, table=True):
    __tablename__ = "room"
    id: int = Field(default=None, primary_key=True)
    name: str
    capacity: int
    localization: str
    stuff: Dict[str, Any] = Field(default=None, sa_column=Column(JSON))
    is_active: bool = True
