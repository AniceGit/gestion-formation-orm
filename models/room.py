from sqlmodel import Field, Session, SQLModel, create_engine

class Room(SQLModel, table=True):
    id_room : int | None = Field(default=None, primary_key=True)
    name : str
    capacity : int
    localization : str
    stuff : dict | str
    is_active : bool = True
    

