from server.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .mixins.upldate_moddate import Mixin as time_mixin
from typing import List
from server import models

class WorkoutRoutine(Base, time_mixin):
    __tablename__ = 'workout_routine'

    xid = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    name = Column(
        String(255),
        nullable=True
    )

    day = Column(
        Integer,
        nullable=False
    )


    is_rest_day = Column(
        Boolean,
        nullable=False,
        default=False
    )
    user_xid: Mapped[int] \
        = mapped_column(
            ForeignKey("user.xid"),
            nullable=False
        )

    # exercise_relationships: Mapped[List["models.WorkoutRoutineExerciseRelationship"]] \
    #     = relationship()
    

    exercise_relationships: Mapped[List["models.WorkoutRoutineExerciseRelationship"]] \
        = relationship(
            'WorkoutRoutineExerciseRelationship',
            # foreign_keys=[]
        )


    # SETS WILL BE A JOIN RELALTIONSHIP


    # start_time_utc = Column(
    #     DateTime(),
    #     nullable=True,
        
    # )

    # end_time_utc = Column(
    #     DateTime(),
    #     nullable=True,
        
    # )

    # deleted_utc = Column(
    #     DateTime(),
    #     nullable=True,
        
    # )

    # user_xid: Mapped[int] \
    #     = mapped_column(
    #         ForeignKey("user.xid"),
    #         nullable=False
    #     )



    # workout_sets: Mapped[List["models.WorkoutSet"]] \
    #     = relationship()
    # SETS WILL BE A JOIN RELALTIONSHIP


# workout_sessionxid
# ! sets [List of ids, 
# 