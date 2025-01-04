from server.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .mixins.upldate_moddate import Mixin as time_mixin
from typing import List
from server import models

class WorkoutSession(Base, time_mixin):
    __tablename__ = 'workout_session'

    xid = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    name = Column(
        String(255),
        nullable=True
    )

    start_time_utc = Column(
        DateTime(),
        nullable=True,
        
    )

    end_time_utc = Column(
        DateTime(),
        nullable=True,
        
    )

    deleted_utc = Column(
        DateTime(),
        nullable=True,
        
    )

    user_xid: Mapped[int] \
        = mapped_column(
            ForeignKey("user.xid"),
            nullable=False
        )



    # workout_sets: Mapped[List["models.WorkoutSet"]] \
    #     = relationship()
    # SETS WILL BE A JOIN RELALTIONSHIP


# workout_sessionxid
# ! sets [List of ids, 
# 