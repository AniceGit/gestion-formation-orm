from db.database import engine
from sqlalchemy.orm import sessionmaker
import datetime as date
from enum import Enum

# schemas
from schemas import learner_schemas as learn_sch
from schemas import teachingstaff_schemas as tstaff_sch
from schemas import trainer_schemas as train_sch
from schemas import admin_schemas as adm_sch
from schemas import room_schemas as room_sch
from schemas import session_schemas as sess_sch
from schemas import inscription_schemas as insc_sch

# crud
from crud import learner_controller as learn_contr
from crud import trainer_controller as train_contr
from crud import teachingstaff_controller as teachstaff_contr

# enum
from models.teachingstaff import TeachingStaffRole as teachstaff_role


def connect_to_session():
    # Connection to db
    engine_session = engine
    Session = sessionmaker(bind=engine_session)
    session = Session()
    return session


def main():
    # Users creation
    new_learner = learn_sch.LearnerCreate(
        name="John",
        firstname="Doe",
        email="john.doe@generator.com",
        birth_date=date.datetime(2009, 6, 6),
        date_create=date.datetime.now().date(),
        phone="+213676424242",
        platform_registration_date=date.datetime.now().date(),
    )

    new_trainer = train_sch.TrainerCreate(
        name="John",
        firstname="Doe",
        email="john.doe@generator.com",
        birth_date=date.datetime(2009, 6, 6),
        date_create=date.datetime.now().date(),
        speciality="DevOps",
        date_hire=date.datetime(2003, 4, 13),
        hourly_rate=14.67,
    )

    new_teachingstaff = teachstaff_contr.TeachingStaffCreate(
        name="John",
        firstname="Doe",
        email="john.doe@generator.com",
        birth_date=date.datetime(1994, 6, 6),
        date_create=date.datetime.now().date(),
        work=teachstaff_role.EDUCATIONAL_MANAGER,
        date_appointement=date.datetime(2000, 4, 13),
        responsabilities={
            "enseignements": "organisation des enseignements",
            "eleves": "orientation et gestion des conseils de classe",
        },
    )

    # Users insert
    learn_contr.add_learner(new_learner, connect_to_session())
    train_contr.add_trainer(new_trainer, connect_to_session())
    teachstaff_contr.add_teachingstaff(new_teachingstaff, connect_to_session())


if __name__ == "__main__":
    main()
