import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.user import UserRole
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, constr, StringConstraints, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
import datetime as date
from dateutil.relativedelta import relativedelta


class LearnerCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)]
    firstname: Annotated[str, StringConstraints(max_length=50)]
    email: EmailStr = Field(unique=True)
    age: Annotated[int, Field(gt=16)]
    date_create: date.date
    role: UserRole
    birth_date: date.date = Field(None, ge=date.date.today() - relativedelta(years=16))
    study_level: Optional[str] = None  # unrequired field
    phone: Optional[PhoneNumber] = None  # unrequired field
    platform_registration_date: date.date = Field(default=date.datetime.now())

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
            "role": UserRole("Learner"),
            "birth_date": date.datetime(2009, 6, 5),
            "platform_registration_date": date.datetime.now().date(),
            "phone": "+213676424242",
        },
        {
            "name": "Jane",
            "firstname": "Doe",
            "email": "jane.doe@generator.com",
            "age": 40,
            "date_create": date.datetime.now().date(),
            "role": UserRole("Learner"),
            "birth_date": date.datetime.now().date(),
            "platform_registration_date": date.datetime.now().date(),
        },
    ]

    new_users = [LearnerCreate(**item) for item in info_user_dict]
    print(new_users[0].name)
    print(new_users[0].phone)


if __name__ == "__main__":
    main()
