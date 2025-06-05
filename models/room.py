from sqlmodel import Field, Session, SQLModel, create_engine


class Room(SQLModel, table=True):
    __tablename__ = "room"
    id: int = Field(default=None, primary_key=True)
    name: str
    capacity: int
    localization: str
    stuff: str
    is_active: bool = True
