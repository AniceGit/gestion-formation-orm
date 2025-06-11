import streamlit as st
import os
import sys
import datetime as dt

# schemas
from schemas import learner_schemas as learn_sch
from schemas import teachingstaff_schemas as tstaff_sch
from schemas import trainer_schemas as train_sch
from schemas import admin_schemas as adm_sch
from schemas import user_schemas as use_sch

# crud
from crud import learner_controller as learn_contr
from crud import trainer_controller as train_contr
from crud import teachingstaff_controller as teachstaff_contr
from crud import admin_controller as admin_contr

# enum

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.user import UserRole
from models.teachingstaff import TeachingStaffRole


# connect
from db.database import engine
from sqlmodel import Session


def connect_to_session():
    return Session(engine)


def display():
    st.set_page_config(page_title="Utilisateur")

    st.title("Page de création d'un utilisateur")
    crud_options = [
        "Créer",
        "Afficher",
        "Modifier",
        "Supprimer",
    ]
    with st.expander("Choisissez votre objectif"):
        crud_choice = st.radio("", crud_options)

    options = [role.value for role in UserRole]
    # Choose actions to do
    with st.expander("Choisissez un rôle"):
        choice_role = st.radio("", options)

    define_choice(choice_role, crud_choice)


def define_choice(choice_role: str, crud_choice: str):
    """_summary_

    Args:
        choice_role (int): _description_
    """
    if choice_role == "Learner":
        if crud_choice == "Créer":
            st.subheader("Création d'un nouvelle apprenant")
            new_learner()
        elif crud_choice == "Afficher":
            st.subheader("Affichage des apprenants")
            show_learner()
        elif crud_choice == "Modifier":
            pass
        elif crud_choice == "Supprimer":
            pass
    elif choice_role == "Trainer":
        if crud_choice == "Créer":
            st.subheader("Création d'un nouvelle enseignant")
            new_trainer()
        elif crud_choice == "Afficher":
            st.subheader("Affichage des enseignants")
            show_trainer()
        elif crud_choice == "Modifier":
            pass
        elif crud_choice == "Supprimer":
            pass
    elif choice_role == "TeachingStaff":
        if crud_choice == "Créer":
            st.subheader("Création d'un nouveau staff pédagogique")
            new_teachingstaff()
        elif crud_choice == "Afficher":
            st.subheader("Affichage des staff pédagogique")
            show_teachingstaff()
        elif crud_choice == "Modifier":
            pass
        elif crud_choice == "Supprimer":
            pass
    elif choice_role == "Admin":
        if crud_choice == "Créer":
            st.subheader("Création d'un nouvelle admin")
            new_admin()
        elif crud_choice == "Afficher":
            st.subheader("Affichage des administrateurs")
            show_admin()
        elif crud_choice == "Modifier":
            pass
        elif crud_choice == "Supprimer":
            pass


# Create
def new_user():
    name = st.text_input("Insérer votre nom")
    firstname = st.text_input("Insérer votre prénom")
    email = st.text_input("Insérer votre email")
    birth_date = st.date_input(
        "Insérer votre date de naissance",
        min_value=dt.date(1975, 1, 1),
    )
    date_create = dt.date.today()
    info_user_dict = {
        "name": name,
        "firstname": firstname,
        "email": email,
        "birth_date": birth_date,
        "date_create": date_create,
    }
    return info_user_dict


def new_learner():
    with st.form("create_user"):
        info_user_dict = new_user()
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
            info_user_dict["role"] = role
            info_user_dict["platform_registration_date"] = platform_registration_date

            if study_levels != []:
                info_user_dict["study_level"] = study_levels
            if phone != "":
                info_user_dict["phone"] = phone
            new_learner = learn_sch.LearnerCreate(**info_user_dict)
            learn_contr.add_learner(new_learner, connect_to_session())
            st.write("Création de l'utilisateur")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


def new_trainer():
    with st.form("create_user"):
        info_user_dict = new_user()
        role = "Learner"
        speciality = st.text_input("Insérer votre spécialité")
        date_hire = dt.date.today()
        hourly_rate = st.number_input("Insérer votre salaire horaire", min_value=0.00)
        bio = ""
        bio = st.text_area("Insérer votre bio (optionel)")
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            info_user_dict["role"] = role
            info_user_dict["speciality"] = speciality
            info_user_dict["date_hire"] = date_hire
            info_user_dict["hourly_rate"] = hourly_rate
            if bio != []:
                info_user_dict["bio"] = bio
            new_learner = train_sch.TrainerCreate(**info_user_dict)
            train_contr.add_trainer(new_learner, connect_to_session())
            st.write("Création de l'utilisateur")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


def new_teachingstaff():
    nb_resp = st.number_input(
        "Nombre de responsabilités", min_value=0, max_value=10, value=0
    )
    with st.form("create_user"):
        info_user_dict = new_user()
        role = "TeachingStaff"
        options_work = [work.value for work in TeachingStaffRole]
        # Choose work
        with st.expander("Choisissez votre travail"):
            choice_work = st.radio("", options_work)
        date_appointement = dt.date.today()
        responsabilities = {}
        for i in range(nb_resp):
            key = st.text_input(f"Type de poste #{i+1}", key=f"key_{i}")
            value = st.text_input(f"Poste #{i+1}", key=f"value_{i}")
            if key:
                responsabilities[key] = value
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            info_user_dict["role"] = role
            info_user_dict["work"] = choice_work
            info_user_dict["date_appointement"] = date_appointement
            if responsabilities != {}:
                info_user_dict["responsabilities"] = responsabilities
            new_teachstaff = tstaff_sch.TeachingStaffCreate(**info_user_dict)
            teachstaff_contr.add_teachingstaff(new_teachstaff, connect_to_session())
            st.write("Création de l'utilisateur")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


def new_admin():
    with st.form("create_user"):
        info_user_dict = new_user()
        role = "Admin"
        options = admin_contr.get_adminrole(connect_to_session())
        option_role = [value.replace("_", " ").title() for _, value in options.items()]
        # Choose work
        with st.expander("Choisissez votre travail"):
            choice_role = st.multiselect("", option_role)
        # access_level = List[int]  # list of AdminRole:id
        promotion_date = dt.date.today()
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            info_user_dict["role"] = role
            info_user_dict["promotion_date"] = promotion_date
            admin_role_list = [role.lower().replace(" ", "_") for role in choice_role]
            access_level = []
            if admin_role_list:
                access_level = [
                    key for key, value in options.items() if value in admin_role_list
                ]
            info_user_dict["access_level"] = access_level
            new_admin = adm_sch.AdminCreate(**info_user_dict)
            admin_contr.add_admin(new_admin, connect_to_session())
            st.write("Création de l'utilisateur")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


# Read
def show_learner():
    learners = learn_contr.get_learner(connect_to_session())
    for learner in learners:
        with st.expander(f"{learner.firstname} {learner.name}"):
            st.text(f"Prénom : {learner.firstname}")
            st.text(f"Prénom : {learner.name}")
            st.text(f"Email : {learner.email}")
            st.text(
                f"Date d'inscription sur la plateforme : {learner.platform_registration_date}"
            )


def show_trainer():
    trainers = train_contr.get_trainer(connect_to_session())
    for trainer in trainers:
        with st.expander(f"{trainer.firstname} {trainer.name}"):
            st.text(f"Prénom : {trainer.firstname}")
            st.text(f"Prénom : {trainer.name}")
            st.text(f"Email : {trainer.email}")
            st.text(f"Date d'embauche : {trainer.date_hire}")


def show_teachingstaff():
    teachingstaffs = teachstaff_contr.get_teachingstaff(connect_to_session())
    for teachingstaff in teachingstaffs:
        with st.expander(f"{teachingstaff.firstname} {teachingstaff.name}"):
            st.text(f"Prénom : {teachingstaff.firstname}")
            st.text(f"Prénom : {teachingstaff.name}")
            st.text(f"Email : {teachingstaff.email}")


def show_admin():
    admins = admin_contr.get_admin(connect_to_session())
    for admin in admins:
        with st.expander(f"{admin.firstname} {admin.name}"):
            st.text(f"Prénom : {admin.firstname}")
            st.text(f"Prénom : {admin.name}")
            st.text(f"Email : {admin.email}")
            st.text(f"Date de promotion : {admin.promotion_date}")


if __name__ == "__main__":
    display()
