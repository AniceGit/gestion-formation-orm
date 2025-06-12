import streamlit as st
import datetime as dt

# schemas
from schemas import inscription_schemas as inscription_sch

# crud
from crud import inscription_controller as inscription_contr


# connect
from db.database import engine
from sqlmodel import Session


def display():
    st.set_page_config(page_title="Inscription")

    st.title("Page d'inscription")
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
        st.subheader("Création d'une nouvelle salle")
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


# Create
def new_inscription():
    pass


# Read
def show_inscription():
    pass


# Update
def update_inscription():
    pass


# Delete
def delete_inscription():
    pass


if __name__ == "__main__":
    display()
