import streamlit as st

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


def display():
    st.set_page_config(layout="wide")
    # Display the title
    st.title(
        "Créer une base de données avec un ORM et une application de gestion de centre de formation"
    )

    with st.form("info_form"):
        st.markdown("### 🎯 Objectif du site")

        st.markdown(
            """
        Vous êtes Data Engineer au sein d’un centre de formation (CF-Tech) qui dispense des cours et ateliers sur les technologies numériques. Jusqu’à présent, les informations concernant les sessions, les salles, les formateurs et les apprenants étaient gérées à la main, au moyen de fichiers Excel et d’un ERP vieillissant. La direction souhaite passer à une solution plus robuste : une base de données relationnelle pilotée par un ORM (SQLAlchemy/SQLModel) avec migrations (Alembic) et validation stricte des données (Pydantic).

        L’objectif est d’avoir un système centralisé capable de :
            - Gérer l’ensemble des utilisateurs de la plateforme (apprenants, formateurs, staff pédagogique, administrateurs).
            - Suivre les sessions de formation (planning, salle, formateur, capacité).
            - Enregistrer les inscriptions des apprenants aux sessions et leur historique d’avancement.
            - Assurer la qualité des données à l’insertion (emails valides, dates cohérentes, plage d’âge, unicité des comptes, etc.).
            - Faire évoluer le schéma au fil des besoins (ajout de nouveaux rôles, champs, etc.) sans interrompre l’exploitation.
        """
        )

        submit_button = st.form_submit_button("Compris ✅")

    is_submit_button_compris(submit_button)


def is_submit_button_compris(submit_button: bool):
    if submit_button:
        st.success("Bonne navigation sur le site !")


if __name__ == "__main__":
    display()
