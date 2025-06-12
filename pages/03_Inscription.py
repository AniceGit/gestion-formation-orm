import streamlit as st
import datetime as dt

# schemas
from schemas import inscription_schemas as inscription_sch
from schemas import room_schemas as room_sch
from schemas import trainer_schemas as train_sch

# crud
from crud import inscription_controller as inscription_contr
from crud import room_controller as room_contr
from crud import trainer_controller as train_contr

# connect
from db.database import engine
from sqlmodel import Session


def display():
    st.set_page_config(page_title="Inscription")

    st.title("Page de formation")
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
    if crud_choice == "Créer":
        st.subheader("Création d'une nouvelle formation")
        new_inscription()
    elif crud_choice == "Afficher":
        st.subheader("Affichage des salles")
        show_inscription()
    elif crud_choice == "Modifier":
        st.subheader("Modification d'une salle")
        update_inscription()
    elif crud_choice == "Supprimer":
        st.subheader("Supprimer une salle")
        delete_inscription()


# Connect to Session
def connect_to_session():
    return Session(engine)


# Create
def define_inscription():
    title = st.text_input("Insérer l'intitulé")
    description = st.text_area("Insérer la description de l'inscription")
    start_date = st.date_input(
        "Insérer la date de début",
        min_value=dt.date(1975, 1, 1),
    )
    end_date = st.date_input(
        "Insérer la date de fin",
        min_value=dt.date(1975, 1, 1),
    )
    max_capacity = st.number_input("Insérer la capacité maximum", min_value=1)
    info_user_dict = {
        "title": title,
        "description": description,
        "start_date": start_date,
        "end_date": end_date,
        "max_capacity": max_capacity,
    }
    return info_user_dict


def new_inscription():
    requires = st.number_input("Nombre d'exigences", min_value=0, max_value=10, value=0)
    with st.form("create_inscription"):
        info_room_dict = define_inscription()
        status = inscription_sch.InscriptionStatusEnum.ENREGISTRE
        require_list = []
        for i in range(requires):
            key = st.text_input(f"Type de poste #{i+1}", key=f"key_{i}")
            if key:
                require_list.append(key)
        info_room_dict["status"] = status
        info_room_dict["stuff"] = require_list

        all_trainer = train_contr.get_trainer(connect_to_session())
        all_trainer_email = [value.email for value in all_trainer]
        # Choose learner
        with st.expander("Choisissez l'enseignant"):
            choice_learner = st.radio("", all_trainer_email)

        all_room = room_contr.get_all_rooms_as_create(connect_to_session())
        all_room_name = [value.name for value in all_room]
        # Choose room
        with st.expander("Choisissez votre salle"):
            choice_room = st.radio("", all_room_name)

        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            st.write("Coming soon ...")
        except:
            pass


# Read
def show_inscription():
    st.image("./assets/coming_soon1.gif")
    st.write(
        "Coming soon n’est pas une promesse, c’est un silence chargé d’avenir. "
        "C’est l’instant suspendu où le présent retient son souffle, où le futur murmure à l’oreille de ceux qui espèrent encore."
    )


# Update
def update_inscription():
    st.image("./assets/coming_soon1.gif")
    st.write(
        "Coming soon n’est pas une promesse, c’est un silence chargé d’avenir. "
        "C’est l’instant suspendu où le présent retient son souffle, où le futur murmure à l’oreille de ceux qui espèrent encore."
    )


# Delete
def delete_inscription():
    st.image("./assets/coming_soon1.gif")
    st.write(
        "Coming soon n’est pas une promesse, c’est un silence chargé d’avenir. "
        "C’est l’instant suspendu où le présent retient son souffle, où le futur murmure à l’oreille de ceux qui espèrent encore."
    )


if __name__ == "__main__":
    display()
