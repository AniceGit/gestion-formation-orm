import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.room import Room
from schemas.room_schemas import RoomCreate, RoomUpdate
from sqlmodel import select, update


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
        statement = select(Room).where(Room.is_active == True)
        results = session.exec(statement).all()
        all_room = [RoomCreate(**item.model_dump()) for item in results]
        return all_room
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la lecture des salles")
        print(f"Exception: {exc}")
        print("-" * 25)
        return []


def del_room(name_room: int, session):
    try:
        statement = (
            update(Room)
            .where(Room.name == name_room)
            .where(Room.is_active == 1)
            .values(is_active=0)
        )
        session.exec(statement)
        session.commit()
        session.close()
    except:
        raise ValueError(f"Aucune salle avec le nom : {name_room}")


def upd_room(learner_obj: RoomUpdate, session_upd_room) -> None:
    try:
        statement = (
            select(Room)
            .where(Room.name == learner_obj.name)
            .where(Room.is_active == True)
        )
        room_info = session_upd_room.exec(statement).first()
        update_fields = learner_obj.model_dump(exclude_unset=True)

        for key, value in update_fields.items():
            setattr(room_info, key, value)

        session_upd_room.add(room_info)
        session_upd_room.commit()
        session_upd_room.close()

    except:
        raise ValueError(f"Aucun apprenant avec l'email : {learner_obj}")
