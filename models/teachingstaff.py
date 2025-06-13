from sqlmodel import Field
from sqlalchemy import Column, JSON
from typing import Optional, Any, Dict
from enum import Enum
from datetime import date
import models.user as u


class TeachingStaffRole(str, Enum):
    """Enumération pour les rôles du personnel enseignant"""

    EDUCATIONAL_MANAGER = "RESPONSABLE PEDAGOGIQUE"
    PROJECT_HANDLER = "CHARGEE DE PROJET"


class TeachingStaff(u.User, table=True):
    """Modèle pour le personnel enseignant, hérite de User"""

    __tablename__ = "teaching_staff"
    __table_args__ = {"extend_existing": True}
    work: TeachingStaffRole  # required field
    date_appointement: date  # required field
    responsabilities: Optional[Dict[str, Any]] = Field(
        default=None, sa_column=Column(JSON)
    )
