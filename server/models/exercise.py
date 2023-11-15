from server.database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .mixins.upldate_moddate import Mixin as time_mixin
from server import models
import json

class Exercise(Base, time_mixin):
    __tablename__ = 'exercise'

    exercise_id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    # stored as json
    # maybe primary:1, secondary0:2, secondary1:3
    # or primary:1, secondary: [2,3]
    target_muscles_json = Column(
        Text(),
        nullable=True
    )
    
    user_id: Mapped[int] \
        = mapped_column(
            ForeignKey("user.user_id"),
            nullable=False
        )

    # user: Mapped["models.User"] \
    #     = relationship(back_populates="trainer_profile")

    @property
    def target_muscles_as_schema(self):
        pass