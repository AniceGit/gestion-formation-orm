from pydantic import BaseModel, Field
from typing import Dict, Any


class RoomCreate(BaseModel):
    name: str
    capacity: int = Field(ge=1)
    localization: str
    stuff: Dict[str, Any]
    is_active: bool = True

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
