from server.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .mixins.upldate_moddate import Mixin as time_mixin
from typing import List
from server import models

class WorkoutRoutineExerciseRelationship(Base, time_mixin):
    __tablename__ = 'workout_routine_exercise_relationship'

    xid = Column(
        Integer,
        primary_key=True,
        nullable=False
    )


    workout_routine_xid: Mapped[int] \
        = mapped_column(
            ForeignKey("workout_routine.xid"),
            nullable=False
        )

    exercise_xid: Mapped[int] \
        = mapped_column(
            ForeignKey("exercise.xid"),
            nullable=True
        )

    exercise: Mapped["models.Exercise"] \
        = relationship(
            'Exercise',
            foreign_keys=[exercise_xid],
            # back_populates="user_demographic",
            single_parent=True
        )
    

    # xid = Column(
    #     Integer,
    #     primary_key=True,
    #     nullable=False
    # )

    # name = Column(
    #     String(255),
    #     nullable=True
    # )

    # day = Column(
    #     Integer,
    #     primary_key=True,
    #     nullable=False
    # )

    
