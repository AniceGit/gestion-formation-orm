import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sqlmodel import SQLModel
from database import engine

from models.user import User
from models.learner import Learner
from models.teachingstaff import TeachingStaff
from models.trainer import Trainer
from models.admin import Admin, AdminAdminRoleLink, AdminRole
from models.room import Room
from models.session import Session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
