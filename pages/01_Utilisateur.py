import streamlit as st
import os
import sys
import datetime as dt

# schemas
from schemas import learner_schemas as learn_sch
from schemas import teachingstaff_schemas as tstaff_sch
from schemas import trainer_schemas as train_sch
from schemas import admin_schemas as adm_sch

# crud
from crud import learner_controller as learn_contr
from crud import trainer_controller as train_contr
from crud import teachingstaff_controller as teachstaff_contr
from crud import admin_controller as admin_contr

# enum

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.user import UserRole


# connect
from db.database import engine
from sqlalchemy.orm import sessionmaker


def connect_to_session():
    # Connection to db
    engine_session = engine
    Session = sessionmaker(bind=engine_session)
    session = Session()
    return session


def display():
    st.set_page_config(page_title="Utilisateur")

    st.title("Page de création d'un utilisateur")

    options = [role.value for role in UserRole]
    # Choose actions to do
    with st.expander("Choisissez un rôle"):
        choice_role = st.radio("", options)

    define_role(choice_role)


def define_role(choice_role: str):
    """_summary_

    0 = "Learner"
    1 = "Trainer"
    2 = "TeachingStaff"
    3 = "Admin"

    Args:
        choice_role (int): _description_
    """
    if choice_role == "Learner":
        st.subheader("Création d'un nouvelle apprenant")
        new_learner()
    elif choice_role == "Trainer":
        st.subheader("Création d'un nouvelle enseignant")
        new_trainer()
    elif choice_role == "TeachingStaff":
        st.subheader("Création d'un nouveau staff pédagogique")
        new_teachingstaff()
    elif choice_role == "Admin":
        st.subheader("Création d'un nouvelle admin")
        new_admin()


def new_learner():
    with st.form("create_user"):
        name = st.text_input("Insérer votre nom")
        firstname = st.text_input("Insérer votre prénom")
        email = st.text_input("Insérer votre email")
        birth_date = st.date_input(
            "Insérer votre date de naissance",
            min_value=dt.date(1975, 1, 1),
        )
        date_create = dt.date.today()
        role = "Learner"
        study_levels = []
        study_levels = st.multiselect(
            "Sélectionnez vos niveaux d'étude (optionel)",
            ["Bac", "Bac+2", "Bac+3", "Master", "Doctorat"],
        )
        phone = st.text_input("Insérer votre numéro de téléphone (optionel)")
        platform_registration_date = dt.date.today()
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            new_learner = learn_sch.LearnerCreate(
                name=name,
                firstname=firstname,
                email=email,
                birth_date=birth_date,
                role=role,
                date_create=date_create,
                platform_registration_date=platform_registration_date,
            )
            if study_levels != []:
                new_learner.study_level = study_levels
            if phone != "":
                new_learner.phone = phone
            learn_contr.add_learner(new_learner, connect_to_session())
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


def new_trainer():
    bio = ""
    speciality = st.text_input("Insérer votre spécialité")
    date_hire = dt.today()
    hourly_rate = st.number_input("Insérer votre temps de travail", min_value=0.00)
    bio = st.text_area("Insérer votre bio (optionel)")
    return (speciality, date_hire, hourly_rate, bio)


def new_teachingstaff():
    pass


def new_admin():
    pass


if __name__ == "__main__":
    display()
