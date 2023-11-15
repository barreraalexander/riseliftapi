from server.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .mixins.upldate_moddate import Mixin as time_mixin

class WorkoutSet(Base, time_mixin):
    __tablename__ = 'workout_set'

    _id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )