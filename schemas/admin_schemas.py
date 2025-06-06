import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.user import UserRole
from typing import Optional, Annotated, List
from pydantic import BaseModel, EmailStr, constr, StringConstraints, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
import datetime as date
from dateutil.relativedelta import relativedelta


class AdminAdminRoleLinkCreate(BaseModel):
    admin_id: int = Field(...)
    role_id: int = Field(...)

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class AdminRoleCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)]

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class AdminCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)]
    firstname: Annotated[str, StringConstraints(max_length=50)]
    email: EmailStr = Field(unique=True)
    birth_date: date.date = Field(None, ge=date.date.today() - relativedelta(years=16))
    date_create: date.date
    role: UserRole = UserRole.user_admin
    access_level: List[int]
    promotion_date: date.date

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
            "access_level": [
                1,
                2,
            ],
            "promotion_date": date.datetime(2009, 6, 5),
        },
        {
            "name": "Jane",
            "firstname": "Doe",
            "email": "jane.doe@generator.com",
            "age": 40,
            "date_create": date.datetime.now().date(),
            "access_level": [
                1,
            ],
            "promotion_date": date.datetime(2009, 6, 5),
        },
    ]

    info_admin_role_dict = [
        {"name": "SUPERADMIN"},
        {"name": "ADMIN_STANDARD"},
    ]

    info_admin_adminrole_link_dict = [
        {
            "admin_id": 1,
            "role_id": 1,
        },
        {
            "admin_id": 1,
            "role_id": 2,
        },
        {
            "admin_id": 2,
            "role_id": 1,
        },
    ]

    new_users = [AdminCreate(**item) for item in info_user_dict]
    print(new_users[0].name)
    print(new_users[0].promotion_date)
    print(new_users[0].access_level)

    new_admin_role = [AdminRoleCreate(**item) for item in info_admin_role_dict]
    print(new_admin_role[0].name)

    new_admin_adminrole_link = [
        AdminAdminRoleLinkCreate(**item) for item in info_admin_adminrole_link_dict
    ]
    print(new_admin_adminrole_link[0].admin_id)
    print(new_admin_adminrole_link[1].admin_id)


if __name__ == "__main__":
    main()
