from server.database import Base
from sqlalchemy import Column, Integer, String

from .mixins.upldate_moddate import Mixin as time_mixin


class WorkoutSession(Base, time_mixin):
    __tablename__ = 'workout_session'

    workout_session_id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    # SETS WILL BE A JOIN RELALTIONSHIP


# workout_session_id
# ! sets [List of ids, 
# 