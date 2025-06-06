import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.user import UserRole
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, constr, StringConstraints, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
import datetime as date
from dateutil.relativedelta import relativedelta


class TrainerCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)]
    firstname: Annotated[str, StringConstraints(max_length=50)]
    email: EmailStr = Field(unique=True)
    birth_date: date.date = Field(None, ge=date.date.today() - relativedelta(years=16))
    date_create: date.date
    role: UserRole = UserRole.user_trainer
    speciality: str
    date_hire: date.date = Field(None, lt=date.date.today())
    hourly_rate: Annotated[float, Field(ge=0.0)]
    bio: Annotated[Optional[str], StringConstraints(max_length=50)] = None

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


def main():
    info_user_dict = [
        {
            "name": "John",
            "firstname": "Doe",
            "email": "john.doe@generator.com",
            "age": 42,
            "date_create": date.datetime.now().date(),
            "speciality": "Data Science",
            "date_hire": date.datetime(2009, 6, 5),
            "hourly_rate": 37.5,
        },
        {
            "name": "Jane",
            "firstname": "Doe",
            "email": "jane.doe@generator.com",
            "age": 40,
            "date_create": date.datetime.now().date(),
            "speciality": "DevOps",
            "date_hire": date.datetime(2014, 6, 5),
            "hourly_rate": 35,
        },
    ]

    new_users = [TrainerCreate(**item) for item in info_user_dict]
    print(new_users[0].name)
    print(new_users[0].email)


if __name__ == "__main__":
    main()
