import faker as fk
from models.admin import Admin
from models.inscription import Inscription
from models.learner import Learner
from models.room import Room
from models.session import Session
from models.teachingstaff import TeachingStaff
from models.trainer import Trainer
from models.user import User

faker = fk.Faker()

def random_element_list(liste):
    return liste[faker.pyint(0, len(liste) -1)]

def generate_fake_admin(nb_admins: int) -> list[Admin]:
    list_result = []
    for _ in range(nb_admins):
        admin = Admin(
            id_user = faker.pyint(),
            # access_level = ,
            promotion_date = faker.date()
        )
        list_result.append(admin)
    return list_result


def generate_fake_inscription(nb_inscriptions) -> list[Inscription]:
    list_result = []
    list_status = ["ENREGISTRE", "DESINSCRIT", "EN_ATTENTE"]
    for _ in range(nb_inscriptions):
        inscription = Inscription(
            inscription_date = faker.date(),
            inscription_status = random_element_list(list_status),
            presence = faker.pyint(0,1),
            id_session = faker.pyint(), 
            id_learner = faker.pyint(),
        )
        list_result.append(inscription)
    return list_result

def generate_fake_learner(nb_learners):
    list_result = []
    for _ in range(nb_learners):
        learner = Learner(
            id_user = faker.pyint(),
            birth_date = faker.date(),
            study_level = faker.pyint(0,1),
            phone = faker.phone_number(),
            platform_registration_date = faker.date(),
        )
        list_result.append(learner)
    return list_result

def generate_fake_room(nb_rooms):
    list_result = []
    for _ in range(nb_rooms):
        room = Room(
            name = faker.name(),
            capacity = faker.pyint(),
            localization = faker.building_name(),
            stuff = faker.sentence(4, True),
            is_active = faker.pyint(0,1),
        )
        list_result.append(room)
    return list_result

def generate_fake_session(nb_sessions):
    list_result = []
    list_status = ["OPEN", "CLOSED", "ARCHIVED"]
    for _ in range(nb_sessions):
        session = Session(
            title = faker.sentence(5, True),
            description = faker.sentence(14, True),
            start_date = faker.date(),
            end_date = faker.date(),
            max_capacity = faker.pyint(),
            status = random_element_list(list_status),
            requirements = ,
            id_trainer = faker.pyint(),
            id_room = faker.pyint(),
        )
        list_result.append(session)
    return list_result

def generate_fake_teachingstaff(nb_teachingstaff):
    list_result = []
    list_role = ["RESPONSABLE PEDAGOGIQUE", "RESPONSABLE PEDAGOGIQUE"]
    for _ in range(nb_teachingstaff):
        teachingStaff = TeachingStaff(
            id_user = faker.pyint(),
            work = random_element_list(list_role),
            date_appointement = faker.date(),
            responsabilities = faker.
        )
        list_result.append(teachingStaff)
    return list_result

def generate_fake_trainer(nb_trainers):
    list_result = []
    for _ in range(nb_trainers):
        trainer = Trainer(
            id_user = faker.pyint(),
            speciality = faker.word(),
            date_hire = faker.date(),
            hourly_rate = faker.pyfloat(),
            bio = faker.sentence(10, True),
        )
        list_result.append(trainer)
    return list_result

def generate_fake_user(nb_users):
    list_result = []
    list_user_role = ["Learner", "Trainer", "TeachingStaff", "Admin"]
    for _ in range(nb_users):
        user = User(
            name = faker.name(),
            firstname = faker.first_name(),
            email = faker.email(),
            age = faker.pyint(18, 79),
            date_create = faker.date(),
            is_active = faker.pyint(0,1),
            role = random_element_list(list_user_role),
        )
        list_result.append(user)
    return list_result
    