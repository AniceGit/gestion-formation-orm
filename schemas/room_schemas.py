from pydantic import BaseModel, Field
from typing import Dict, Any, Optional


class RoomCreate(BaseModel):
    """Schema pour créer une salle."""

    name: str
    capacity: int = Field(ge=1)
    localization: str
    stuff: Dict[str, Any]
    is_active: bool = True

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True


class RoomUpdate(BaseModel):
    """Schema pour mettre à jour une salle."""

    name: Optional[str] = None
    capacity: Optional[int] = None
    localization: Optional[str] = None
    stuff: Optional[Dict[str, Any]] = None

    class Config:
        str_strip_whitespace = True
        str_to_lower = True
        frozen = True
