import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.room import Room
from schemas.room_schemas import RoomCreate


def add_room(room_obj: RoomCreate, session_add_room) -> None:
    try:
        new_room = Room(**room_obj.model_dump())

        session_add_room.add(new_room)
        session_add_room.commit()

        print(f"Room: {new_room.id}")
        session_add_room.close()

    except Exception as exc:
        print("-" * 25)
        print("La salle n'a pas été ajoutée")
        print(f"Exception: {exc}")
        print("-" * 25)


def get_all_rooms_as_create(session) -> list[RoomCreate]:
    try:
        list_result = []
        # list of all Room in session
        rooms = session.query(Room).all()
        # Conversion Room -> RoomCreate
        for room in rooms:
            create_room = RoomCreate(**room.model_dump())
            list_result.append(create_room)
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la lecture des salles")
        print(f"Exception: {exc}")
        print("-" * 25)
        return []
