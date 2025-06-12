import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.session import Session
from schemas.session_schemas import SessionCreate
from sqlmodel import select

# region create


def add_session(session_obj: SessionCreate, session_add_session) -> None:
    try:
        new_session = Session(**session_obj.model_dump())

        session_add_session.add(new_session)
        session_add_session.commit()

        print(f"Session: {new_session.id}")
        session_add_session.close()

    except Exception as exc:
        print("-" * 25)
        print("La session n'a pas été ajoutée")
        print(f"Exception: {exc}")
        print("-" * 25)


# region read


def get_all_sessions_as_create(session_global) -> list[SessionCreate]:
    try:
        statement = select(Session).where(Session.is_active == 1)
        list_result = []
        # list of all Session in session
        sessions = session.exec(statement).all()
        # Conversion Session -> SessionCreate
        for session in sessions:
            create_session = SessionCreate(**session.model_dump())
            list_result.append(create_session)
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la lecture des sessions")
        print(f"Exception: {exc}")
        print("-" * 25)
        return []


# region delete


def delete_session_by_attr(attri: str, value: any, session) -> bool:
    try:
        session = (
            session.exec(select(Session))
            .filter(getattr(Session, attri) == value)
            .first()
        )
        if session:
            session_title = session.title
            session.delete(session)
            session.commit()
            print(f"Session supprimée : {session_title}")
            return True
        else:
            print(
                f"Aucune session trouvée avec l'attribut: {attri} ayant la valeur : {value}"
            )
            return False
    except Exception as exc:
        print("-" * 25)
        print("Erreur lors de la suppression de la session")
        print(f"Exception: {exc}")
        print("-" * 25)
        return False
