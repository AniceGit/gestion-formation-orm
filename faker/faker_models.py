import faker as fk
from config import (
    NBR_ADMIN,
    NBR_INSCRIPTION,
    NBR_LEARNER,
    NBR_ROOM,
    NBR_SESSION,
    NBR_TEACHINGSTAFF,
    NBR_TRAINER,
    NBR_USER,
    NBR_ROLE,
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
    return liste[faker.pyint(0, len(liste) - 1)]


# region user


# create a dict to be injected in child class
def generate_fake_user() -> dict[str, any]:
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


def generate_fake_admin(nb_admins: int = NBR_ADMIN) -> list[AdminCreate]:
    list_result = []
    for _ in range(nb_admins):
        user_attributes = generate_fake_user()
        admin = AdminCreate(
            **user_attributes,
            role="Admin",
            id_user=faker.pyint(1, NBR_USER),
            # access_level = ,
            promotion_date=faker.date(),
        )
        list_result.append(admin)
    return list_result

def generate_fake_adminadmin(nb_admins: int = NBR_ADMIN, nb_roles: int = NBR_ROLE) -> list[AdminAdminRoleLinkCreate]:
    """
    tous les admins doivent être dedans
    certains ont plusieurs roles
    """
    list_result = []
    for _ in range(nb_admins):
        for _ in range(faker.pyint(1,nb_roles)):


# region inscription


def generate_fake_inscription(
    nb_inscriptions: int = NBR_INSCRIPTION,
) -> list[InscriptionCreate]:
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


# region learner


def generate_fake_learner(nb_learners=NBR_LEARNER):
    list_result = []
    for _ in range(nb_learners):
        user_attributes = generate_fake_user()
        learner = LearnerCreate(
            **user_attributes,
            role="Learner",
            id_user=faker.pyint(1, NBR_USER),
            study_level=faker.pyint(0, 1),
            phone=faker.phone_number(),
            platform_registration_date=faker.date(),
        )
        list_result.append(learner)
    return list_result


# region room


def generate_fake_room(nb_rooms=NBR_ROOM):
    list_result = []
    for _ in range(nb_rooms):
        room = RoomCreate(
            name=faker.name(),
            capacity=faker.pyint(),
            localization=faker.building_name(),
            stuff=faker.sentence(4, True),
            is_active=faker.pyint(0, 1),
        )
        list_result.append(room)
    return list_result


# region session


def generate_fake_session(nb_sessions=NBR_SESSION):
    list_result = []
    list_status = ["OPEN", "CLOSED", "ARCHIVED"]
    for _ in range(nb_sessions):
        session = SessionCreate(
            title=faker.sentence(5, True),
            description=faker.sentence(14, True),
            start_date=faker.date(),
            end_date=faker.date(),
            max_capacity=faker.pyint(),
            status=random_element_list(list_status),
            # requirements = ,
            id_trainer=faker.pyint(1, NBR_TRAINER),
            id_room=faker.pyint(1, NBR_ROOM),
        )
        list_result.append(session)
    return list_result


# region teachin


def generate_fake_teachingstaff(nb_teachingstaff=NBR_TEACHINGSTAFF):
    list_result = []
    list_role = ["RESPONSABLE PEDAGOGIQUE", "RESPONSABLE PEDAGOGIQUE"]
    for _ in range(nb_teachingstaff):
        user_attributes = generate_fake_user()
        teachingStaff = TeachingStaffCreate(
            **user_attributes,
            role="TeachingStaff",
            id_user=faker.pyint(1, NBR_USER),
            work=random_element_list(list_role),
            date_appointement=faker.date(),
            # responsabilities = faker.
        )
        list_result.append(teachingStaff)
    return list_result


# region trainer


def generate_fake_trainer(nb_trainers=NBR_TRAINER):
    list_result = []
    for _ in range(nb_trainers):
        user_attributes = generate_fake_user()
        trainer = TrainerCreate(
            **user_attributes,
            role="Trainer",
            id_user=faker.pyint(1, NBR_USER),
            speciality=faker.word(),
            date_hire=faker.date(),
            hourly_rate=faker.pyfloat(),
            bio=faker.sentence(10, True),
        )
        list_result.append(trainer)
    return list_result
