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
    """
    Définit les actions à effectuer en fonction du rôle et de l'option CRUD choisie.

    Args:
        choice_role (str): Le rôle de l'utilisateur (Learner, Trainer, TeachingStaff, Admin).
        crud_choice (str): L'option CRUD choisie (Créer, Afficher, Modifier, Supprimer).

    Returns:
        None
    """
    if choice_role == "Learner":
        if crud_choice == "Créer":
            st.subheader("Création d'un nouvelle apprenant")
            new_learner()
        elif crud_choice == "Afficher":
            st.subheader("Affichage des apprenants")
            show_learner()
        elif crud_choice == "Modifier":
            st.subheader("Modification apprenant")
            update_learner()
        elif crud_choice == "Supprimer":
            st.subheader("Supprimer un apprenant")
            delete_learner()
    elif choice_role == "Trainer":
        if crud_choice == "Créer":
            st.subheader("Création d'un nouvelle enseignant")
            new_trainer()
        elif crud_choice == "Afficher":
            st.subheader("Affichage des enseignants")
            show_trainer()
        elif crud_choice == "Modifier":
            st.subheader("Modification enseignant")
            update_trainer()
        elif crud_choice == "Supprimer":
            st.subheader("Supprimer un enseignant")
            delete_trainer()
    elif choice_role == "TeachingStaff":
        if crud_choice == "Créer":
            st.subheader("Création d'un nouveau staff pédagogique")
            new_teachingstaff()
        elif crud_choice == "Afficher":
            st.subheader("Affichage des staff pédagogique")
            show_teachingstaff()
        elif crud_choice == "Modifier":
            st.subheader("Modification staff pédagogique")
            update_teachingstaff()
        elif crud_choice == "Supprimer":
            st.subheader("Supprimer un staff pédagogique")
            delete_teachingstaff()
    elif choice_role == "Admin":
        if crud_choice == "Créer":
            st.subheader("Création d'un nouvelle admin")
            new_admin()
        elif crud_choice == "Afficher":
            st.subheader("Affichage des administrateurs")
            show_admin()
        elif crud_choice == "Modifier":
            st.subheader("Modification admin")
            update_admin()
        elif crud_choice == "Supprimer":
            st.subheader("Supprimer un admin")
            delete_admin()


# Connect to Session
def connect_to_session():
    """Connection à la session de la base de données."""
    return Session(engine)


# Create
def new_user():
    """Crée un nouveau dictionnaire d'informations utilisateur.

    Returns:
        dict: Un dictionnaire contenant les informations de l'utilisateur.
    """
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
    """Crée un nouveau dictionnaire d'informations pour un apprenant."""
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
    """Crée un nouveau dictionnaire d'informations pour un enseignant."""
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
    """Crée un nouveau dictionnaire d'informations pour un membre du personnel pédagogique."""
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
            key = st.text_input(f"Type de poste #{i + 1}", key=f"key_{i}")
            value = st.text_input(f"Poste #{i + 1}", key=f"value_{i}")
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
    """Crée un nouveau dictionnaire d'informations pour un administrateur."""
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
    """Affiche les informations des apprenants."""
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
    """Affiche les informations des enseignants."""
    trainers = train_contr.get_trainer(connect_to_session())
    for trainer in trainers:
        with st.expander(f"{trainer.firstname} {trainer.name}"):
            st.text(f"Prénom : {trainer.firstname}")
            st.text(f"Prénom : {trainer.name}")
            st.text(f"Email : {trainer.email}")
            st.text(f"Date d'embauche : {trainer.date_hire}")


def show_teachingstaff():
    """Affiche les informations des membres du personnel pédagogique."""
    admins = teachstaff_contr.get_teachingstaff(connect_to_session())
    for admin in admins:
        with st.expander(f"{admin.firstname} {admin.name}"):
            st.text(f"Prénom : {admin.firstname}")
            st.text(f"Prénom : {admin.name}")
            st.text(f"Email : {admin.email}")


def show_admin():
    """Affiche les informations des administrateurs."""
    admins = admin_contr.get_admin(connect_to_session())
    for admin in admins:
        with st.expander(f"{admin.firstname} {admin.name}"):
            st.text(f"Prénom : {admin.firstname}")
            st.text(f"Prénom : {admin.name}")
            st.text(f"Email : {admin.email}")
            st.text(f"Date de promotion : {admin.promotion_date}")


# Delete
def delete_learner():
    """Supprime un apprenant en le marquant comme inactif."""
    with st.form("delete_user"):
        email = st.text_input("Insérer votre email")
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            learn_contr.del_learner(email, connect_to_session())
            st.write("Utilisateur archivé")
        except:
            st.error("L'email n'existe pas en base")


def delete_trainer():
    """Supprime un enseignant en le marquant comme inactif."""
    with st.form("delete_user"):
        email = st.text_input("Insérer votre email")
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            train_contr.del_trainer(email, connect_to_session())
            st.write("Utilisateur archivé")
        except:
            st.error("L'email n'existe pas en base")


def delete_teachingstaff():
    """Supprime un membre du personnel pédagogique en le marquant comme inactif."""
    with st.form("delete_user"):
        email = st.text_input("Insérer votre email")
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            teachstaff_contr.del_teachingstaff(email, connect_to_session())
            st.write("Utilisateur archivé")
        except:
            st.error("L'email n'existe pas en base")


def delete_admin():
    """Supprime un administrateur en le marquant comme inactif."""
    with st.form("delete_user"):
        email = st.text_input("Insérer votre email")
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            admin_contr.del_admin(email, connect_to_session())
            st.write("Utilisateur archivé")
        except:
            st.error("L'email n'existe pas en base")


# Update
def update_user():
    """Crée un nouveau dictionnaire d'informations utilisateur pour la mise à jour.

    Returns:
        dict: Un dictionnaire contenant les informations de l'utilisateur à mettre à jour.
    """
    name = st.text_input("Insérer votre nom")
    firstname = st.text_input("Insérer votre prénom")
    email = st.text_input("Insérer le mail de l'utilisateur à modifier*")

    info_user_dict = {
        "name": name,
        "firstname": firstname,
        "email": email,
    }
    return info_user_dict


def update_learner():
    """Met à jour les informations d'un apprenant."""
    with st.form("create_user"):
        info_user_dict = new_user()
        study_levels = []
        study_levels = st.multiselect(
            "Sélectionnez vos niveaux d'étude (optionel)",
            ["Bac", "Bac+2", "Bac+3", "Master", "Doctorat"],
        )
        phone = st.text_input("Insérer votre numéro de téléphone (optionel)")
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            if study_levels != []:
                info_user_dict["study_level"] = study_levels
            if phone != "":
                info_user_dict["phone"] = phone
            filtered_data = {k: v for k, v in info_user_dict.items() if v != ""}
            upd_learner = learn_sch.LearnerUpdate(**filtered_data)
            learn_contr.upd_learner(upd_learner, connect_to_session())
            st.write("Modification de l'utilisateur")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


def update_trainer():
    """Met à jour les informations d'un enseignant."""
    with st.form("create_user"):
        info_user_dict = new_user()
        speciality = st.text_input("Insérer votre spécialité")
        hourly_rate = st.number_input("Insérer votre salaire horaire", min_value=0.00)
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            info_user_dict["speciality"] = speciality
            info_user_dict["hourly_rate"] = hourly_rate
            filtered_data = {k: v for k, v in info_user_dict.items() if v != ""}
            upd_learner = train_sch.TrainerUpdate(**filtered_data)
            train_contr.upd_trainer(upd_learner, connect_to_session())
            st.write("Modification de l'utilisateur")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


def update_teachingstaff():
    """Met à jour les informations d'un membre du personnel pédagogique."""
    with st.form("create_user"):
        info_user_dict = new_user()
        options_work = [work.value for work in TeachingStaffRole]
        # Choose work
        with st.expander("Choisissez votre travail"):
            choice_work = st.radio("", options_work)
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            info_user_dict["work"] = choice_work
            filtered_data = {k: v for k, v in info_user_dict.items() if v != ""}
            upd_learner = tstaff_sch.TeachingStaffUpdate(**filtered_data)
            teachstaff_contr.upd_teachingstaff(upd_learner, connect_to_session())
            st.write("Modification de l'utilisateur")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


def update_admin():
    """Met à jour les informations d'un administrateur."""
    with st.form("create_user"):
        info_user_dict = new_user()
        submit_coo = st.form_submit_button("Valider")

    if submit_coo:
        try:
            filtered_data = {k: v for k, v in info_user_dict.items() if v != ""}
            upd_learner = adm_sch.AdminUpdate(**filtered_data)
            admin_contr.upd_admin(upd_learner, connect_to_session())
            st.write("Modification de l'utilisateur")
        except:
            st.error("Une erreur est survenue. Vérifier vos informations.")


if __name__ == "__main__":
    display()
