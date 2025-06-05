import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.user import UserRole
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, constr, StringConstraints, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
import datetime as date
from dateutil.relativedelta import relativedelta
from typing import Dict, Any
from sqlalchemy import Column, JSON


class RoomCreate(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)] = Field(unique=True)
    capacity: int = Field(None, ge=1)
    localization: str
    stuff: Optional[Dict[str,Any]] = None

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


def main():
    info_room_dict = [
        {
            "name": "R-101",
            "capacity": 30,
            "localization": "Bâtiment A, Étage 1",
            "stuff": {"video_projecteur": True, "tableau": "blanc"},
        },
        {
            "name": "R-201",
            "capacity": 45,
            "localization": "Bâtiment B, Étage 2",
            "stuff": {"video_projecteur": False, "tableau": "blanc"},
        },
    ]

    new_users = [RoomCreate(**item) for item in info_room_dict]
    print(new_users[0].name)
    print(new_users[0].stuff.items())


if __name__ == "__main__":
    main()