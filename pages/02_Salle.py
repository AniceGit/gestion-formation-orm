import streamlit as st
import datetime as dt

# schemas
from schemas import room_schemas as room_sch

# crud
from crud import room_controller as room_contr


# connect
from db.database import engine
from sqlmodel import Session


def display():
    """Affiche la page des salles"""
    st.set_page_config(page_title="Salle")

    st.title("Page des salles")
    crud_options = [
        "Créer",
        "Afficher",
        "Modifier",
        "Supprimer",
    ]
    with st.expander("Choisissez votre objectif"):
        crud_choice = st.radio("", crud_options)

    define_choice(crud_choice)


def define_choice(crud_choice: str):
    """Définit l'action à effectuer en fonction du choix de l'utilisateur"""
    if crud_choice == "Créer":
        st.subheader("Création d'une nouvelle salle")
        new_room()
    elif crud_choice == "Afficher":
        st.subheader("Affichage des salles")
        show_room()
    elif crud_choice == "Modifier":
        st.subheader("Modification d'une salle")
        update_room()
    elif crud_choice == "Supprimer":
        st.subheader("Supprimer une salle")
        delete_room()


# Connect to Session
def connect_to_session():
    """Connection à la base de données"""
    return Session(engine)


# Create
def define_room():
    """Définit les informations de la salle"""
    name = st.text_input("Insérer le nom")
    capacity = st.number_input("Insérer votre capacité", min_value=1)
    localization = st.text_input("Insérer la localisation")
    info_user_dict = {
        "name": name,
        "capacity": capacity,
        "localization": localization,
    }
    return info_user_dict


def new_room():
    """Création d'une nouvelle salle"""
    stuffs = st.number_input("Nombre d'équipements", min_value=0, max_value=10, value=0)
    with st.form("create_room"):
        info_room_dict = define_room()
        stuffs_dict = {}
        for i in range(stuffs):
            key = st.text_input(f"Type d'équipement #{i + 1}", key=f"key_{i}")
            value = st.number_input(
                f"Nombre d'équipement #{i + 1}", min_value=1, key=f"value_{i}"
            )
            if key:
                stuffs_dict[key] = value
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            if stuffs_dict != {}:
                info_room_dict["stuff"] = stuffs_dict
            new_room_object = room_sch.RoomCreate(**info_room_dict)
            room_contr.add_room(new_room_object, connect_to_session())
            st.write("Création de la salle")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


# Read
def show_room():
    """Affichage des salles"""
    rooms = room_contr.get_all_rooms_as_create(connect_to_session())
    for room in rooms:
        with st.expander(f"{room.name}"):
            st.text(f"Nom : {room.name}")
            st.text(f"Capacité : {room.capacity}")
            st.text(f"Localisation : {room.localization}")


# Update
def update_room():
    """Modification d'une salle"""
    stuffs = st.number_input("Nombre d'équipements", min_value=0, max_value=10, value=0)
    with st.form("update_room"):
        info_room_dict = define_room()
        stuffs_dict = {}
        for i in range(stuffs):
            key = st.text_input(f"Type d'équipement #{i + 1}", key=f"key_{i}")
            value = st.number_input(
                f"Nombre d'équipement #{i + 1}", min_value=1, key=f"value_{i}"
            )
            if key:
                stuffs_dict[key] = value
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            if stuffs_dict != {}:
                info_room_dict["stuff"] = stuffs_dict
            filtered_data = {
                k: v for k, v in info_room_dict.items() if v != "" and v != 1
            }
            new_room_object = room_sch.RoomUpdate(**filtered_data)
            room_contr.upd_room(new_room_object, connect_to_session())
            st.write("Modification de la salle")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


# Delete
def delete_room():
    """Suppression d'une salle"""
    rooms = room_contr.get_all_rooms_as_create(connect_to_session())
    info_room = [room.name for room in rooms]
    with st.form("create_room"):
        with st.expander("Choisissez votre salle à modifier"):
            crud_choice = st.radio("", info_room)
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        room_contr.del_room(crud_choice, connect_to_session())


if __name__ == "__main__":
    display()
