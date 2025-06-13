import sys
import os
import phonenumbers

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import faker as fk
from random import shuffle
from config import (
    NBR_ADMIN,
    NBR_INSCRIPTION,
    NBR_LEARNER,
    NBR_ROOM,
    NBR_SESSION,
    NBR_TEACHINGSTAFF,
    NBR_TRAINER,
    NBR_USER,
    LISTE_ROLES_ADMIN,
    STUFF_DICT,
    STAFF_RESPONSIBILITIES,
)
from schemas.admin_schemas import AdminCreate, AdminAdminRoleLinkCreate
from schemas.inscription_schemas import InscriptionCreate
from schemas.learner_schemas import LearnerCreate
from schemas.room_schemas import RoomCreate
from schemas.session_schemas import SessionCreate
from schemas.teachingstaff_schemas import TeachingStaffCreate
from schemas.trainer_schemas import TrainerCreate

faker = fk.Faker()


# function used several times
def random_element_list(liste):
    """
    Retourne un élément aléatoire d'une liste donnée.

    Args:
        liste (list): La liste à partir de laquelle un élément sera sélectionné.

    Returns:
        any: Un élément aléatoire de la liste.
    """
    return liste[faker.pyint(0, len(liste) - 1)]


# region user


# create a dict to be injected in child class
def generate_fake_user() -> dict[str, any]:
    """
    Génère des données utilisateur factices.

    Returns:
        dict[str, any]: Un dictionnaire contenant des informations utilisateur factices.
    """
    user_data = {
        "name": faker.name(),
        "firstname": faker.first_name(),
        "email": faker.email(),
        "birth_date": faker.date_of_birth(minimum_age=16),
        "date_create": faker.date(),
        "is_active": faker.pyint(0, 1),
    }
    return user_data


# region admin


def generate_fake_admin(
    nb_admins: int = NBR_ADMIN, liste_role_admin=LISTE_ROLES_ADMIN
) -> list[AdminCreate]:
    """
    Génère une liste d'administrateurs factices.

    Args:
        nb_admins (int): Le nombre d'administrateurs à générer.
        liste_role_admin (list): La liste des rôles d'administrateur disponibles.

    Returns:
        list[AdminCreate]: Une liste d'objets AdminCreate contenant les informations des administrateurs.
    """
    list_result = []
    list_id = list(range(1, len(liste_role_admin) + 1))
    for _ in range(nb_admins):
        # creation list of a random number of different id available
        list_access_level = []
        shuffle(list_id)
        for i in range(faker.pyint(0, len(liste_role_admin))):
            list_access_level.append(list_id[i])

        user_attributes = generate_fake_user()
        admin = AdminCreate(
            **user_attributes,
            role="Admin",
            access_level=list_access_level,
            promotion_date=faker.date_object(),
        )
        list_result.append(admin)
    return list_result


list_admin = generate_fake_admin()


def generate_fake_adminadmin(
    liste_role_admin=LISTE_ROLES_ADMIN, nb_admins: int = NBR_ADMIN
) -> list[AdminAdminRoleLinkCreate]:
    """
    Génère une liste de liaisons entre les administrateurs et leurs rôles.

    Args:
        liste_role_admin (list): La liste des rôles d'administrateur disponibles.
        nb_admins (int): Le nombre d'administrateurs à générer des liaisons.

    Returns:
        list[AdminAdminRoleLinkCreate]: Une liste d'objets AdminAdminRoleLinkCreate contenant les liaisons entre les administrateurs et leurs rôles.
    """
    list_result = []
    list_id = list(range(1, len(liste_role_admin) + 1))
    for i in range(1, nb_admins + 1):
        user_attributes = generate_fake_user()
        for j in range(faker.pyint(1, len(liste_role_admin))):
            shuffle(list_id)
            adminadmin = AdminAdminRoleLinkCreate(
                **user_attributes, admin_id=i, role_id=list_id[j]
            )
            list_result.append(adminadmin)
    return list_result


liste_adminadmin = generate_fake_adminadmin()

# region inscription


def generate_fake_inscription(
    nb_inscriptions: int = NBR_INSCRIPTION,
) -> list[InscriptionCreate]:
    """
    Génère une liste d'inscriptions factices.

    Args:
        nb_inscriptions (int): Le nombre d'inscriptions à générer.

    Returns:
        list[InscriptionCreate]: Une liste d'objets InscriptionCreate contenant les informations des inscriptions.
    """
    list_result = []
    list_status = ["ENREGISTRE", "DESINSCRIT", "EN_ATTENTE"]
    for _ in range(nb_inscriptions):
        inscription = InscriptionCreate(
            inscription_date=faker.date(),
            inscription_status=random_element_list(list_status),
            presence=faker.pyint(0, 1),
            id_session=faker.pyint(1, NBR_SESSION),
            id_learner=faker.pyint(1, NBR_LEARNER),
        )
        list_result.append(inscription)
    return list_result


liste_inscription = generate_fake_inscription()


# region learner


# create a valid phone number for pydantic
def generate_valid_french_mobile():
    """
    Génère un numéro de téléphone mobile français valide.

    Returns:
        str: Un numéro de téléphone mobile français valide au format international.
    """
    # for french nuber, start by 6 or 7
    first_digit = faker.random_element(elements=("6", "7"))
    rest = faker.numerify("########")  # 8 numbers
    national_number = f"{first_digit}{rest}"
    phone_number = f"+33{national_number}"
    # check phonenumbers
    parsed = phonenumbers.parse(phone_number, None)  # return a PhoneNumber object
    if phonenumbers.is_valid_number(parsed):
        return phone_number
    else:
        # try until found a correct one
        return generate_valid_french_mobile()


def generate_fake_learner(nb_learners=NBR_LEARNER):
    """
    Génère une liste d'apprenants factices.

    Args:
        nb_learners (int): Le nombre d'apprenants à générer.

    Returns:
        list[LearnerCreate]: Une liste d'objets LearnerCreate contenant les informations des apprenants.
    """
    list_result = []
    for _ in range(nb_learners):
        phone = generate_valid_french_mobile()
        user_attributes = generate_fake_user()
        learner = LearnerCreate(
            **user_attributes,
            role="Learner",
            id_user=faker.pyint(1, NBR_USER),
            study_level=faker.word(),
            phone=phone,
            platform_registration_date=faker.date(),
        )
        list_result.append(learner)
    return list_result


liste_learner = generate_fake_learner()


# region room


def generate_fake_room(nb_rooms=NBR_ROOM, stuff_dict=STUFF_DICT):
    """
    Génère une liste de salles factices.

    Args:
        nb_rooms (int): Le nombre de salles à générer.
        stuff_dict (dict): Un dictionnaire contenant les équipements des salles.

    Returns:
        list[RoomCreate]: Une liste d'objets RoomCreate contenant les informations des salles.
    """
    list_result = []
    for _ in range(nb_rooms):
        for key in stuff_dict.keys():
            stuff_dict[key] = faker.boolean()
        room = RoomCreate(
            name=faker.name(),
            capacity=faker.pyint(1, 35),
            localization=faker.word(),
            stuff=stuff_dict,
            is_active=faker.pyint(0, 1),
        )
        list_result.append(room)
    return list_result


liste_room = generate_fake_room()

# region session


def generate_fake_session(nb_sessions=NBR_SESSION):
    """
    Génère une liste de sessions factices.

    Args:
        nb_sessions (int): Le nombre de sessions à générer.

    Returns:
        list[SessionCreate]: Une liste d'objets SessionCreate contenant les informations des sessions.
    """
    list_result = []
    list_status = ["OPEN", "CLOSED", "ARCHIVED"]
    for _ in range(nb_sessions):
        # create a list of requirement, random number between 1 and 7
        list_requirements = []
        for _ in range(faker.pyint(1, 7)):
            list_requirements.append(faker.word())

        # create dates outside of objet because end_date needs start_date
        start_date = faker.date_object()
        end_date = faker.date_between_dates(date_start=start_date)

        session = SessionCreate(
            title=faker.sentence(5, True),
            description=faker.sentence(14, True),
            start_date=start_date,
            end_date=end_date,
            max_capacity=faker.pyint(),
            status=random_element_list(list_status),
            requirements=list_requirements,
            id_trainer=faker.pyint(1, NBR_TRAINER),
            id_room=faker.pyint(1, NBR_ROOM),
        )
        list_result.append(session)
    return list_result


liste_session = generate_fake_session()

# region teachin


def generate_fake_teachingstaff(
    nb_teachingstaff=NBR_TEACHINGSTAFF, dict_responsibilities=STAFF_RESPONSIBILITIES
):
    """
    Génère une liste de membres du personnel enseignant factices.

    Args:
        nb_teachingstaff (int): Le nombre de membres du personnel enseignant à générer.
        dict_responsibilities (dict): Un dictionnaire contenant les responsabilités des membres du personnel enseignant.

    Returns:
        list[TeachingStaffCreate]: Une liste d'objets TeachingStaffCreate contenant les informations des membres du personnel enseignant.
    """
    list_result = []
    list_role = ["RESPONSABLE PEDAGOGIQUE", "RESPONSABLE PEDAGOGIQUE"]
    for _ in range(nb_teachingstaff):
        for key in dict_responsibilities.keys():
            dict_responsibilities[key] = faker.boolean()
        user_attributes = generate_fake_user()
        teachingStaff = TeachingStaffCreate(
            **user_attributes,
            role="TeachingStaff",
            id_user=faker.pyint(1, NBR_USER),
            work=random_element_list(list_role),
            date_appointement=faker.date(),
            responsabilities=dict_responsibilities,
        )
        list_result.append(teachingStaff)
    return list_result


list_teachingstaff = generate_fake_teachingstaff()

# region trainer


def generate_fake_trainer(nb_trainers=NBR_TRAINER):
    """
    Génère une liste de formateurs factices.

    Args:
        nb_trainers (int): Le nombre de formateurs à générer.

    Returns:
        list[TrainerCreate]: Une liste d'objets TrainerCreate contenant les informations des formateurs.
    """
    list_result = []
    for _ in range(nb_trainers):
        user_attributes = generate_fake_user()
        trainer = TrainerCreate(
            **user_attributes,
            role="Trainer",
            id_user=faker.pyint(1, NBR_USER),
            speciality=faker.word(),
            date_hire=faker.date(),
            hourly_rate=faker.pyfloat(min_value=0),
            bio=faker.sentence(10, True),
        )
        list_result.append(trainer)
    return list_result


list_trainer = generate_fake_trainer()
