from typing import Optional
from datetime import date
import models.user as u


class Learner(u.User, table=True):
    """Modèle pour les apprenants, hérite de User"""

    __tablename__ = "learner"
    __table_args__ = {"extend_existing": True}
    study_level: Optional[str]  # unrequired field
    phone: Optional[str]  # unrequired field
    platform_registration_date: date  # required field
