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
    st.set_page_config(page_title="Salle")

    st.title("Page des sessions")
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
        new_session()
    elif crud_choice == "Afficher":
        st.subheader("Affichage des salles")
        show_session()
    elif crud_choice == "Modifier":
        st.subheader("Modification d'une salle")
        update_session()
    elif crud_choice == "Supprimer":
        st.subheader("Supprimer une salle")
        delete_session()


# Create
def new_session():
    st.image("./assets/coming_soon1.gif")
    st.write(
        "Ce qui vient n’appartient encore à personne. Coming soon est l’antichambre de "
        "l’inconnu, l’espace où les rêves prennent forme avant d’oser exister."
    )


# Read
def show_session():
    st.image("./assets/coming_soon1.gif")
    st.write(
        "Ce qui vient n’appartient encore à personne. Coming soon est l’antichambre de "
        "l’inconnu, l’espace où les rêves prennent forme avant d’oser exister."
    )


# Update
def update_session():
    st.image("./assets/coming_soon1.gif")
    st.write(
        "Ce qui vient n’appartient encore à personne. Coming soon est l’antichambre de "
        "l’inconnu, l’espace où les rêves prennent forme avant d’oser exister."
    )


# Delete
def delete_session():
    st.image("./assets/coming_soon1.gif")
    st.write(
        "Ce qui vient n’appartient encore à personne. Coming soon est l’antichambre de "
        "l’inconnu, l’espace où les rêves prennent forme avant d’oser exister."
    )


if __name__ == "__main__":
    display()
