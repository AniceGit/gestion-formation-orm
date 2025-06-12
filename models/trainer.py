from typing import Optional
from datetime import date
import models.user as u


class Trainer(u.User, table=True):
    """Modèle pour les formateurs, hérite de User"""

    __tablename__ = "trainer"
    __table_args__ = {"extend_existing": True}
    speciality: str  # required field
    date_hire: date  # required field
    hourly_rate: float  # required field
    bio: Optional[str]
