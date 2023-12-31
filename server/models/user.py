from server.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from server import models

from .mixins.upldate_moddate import Mixin as time_mixin

class User(Base, time_mixin):
    __tablename__ = 'user'

    xid = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    
    first_name = Column(
        String(255),
        nullable=False
    )
    
    last_name = Column(
        String(255),
        nullable=True
    )

    display_name = Column(
        String(255),
        nullable=True
    )
    
    email = Column(
        String(255),
        nullable=False,
        unique=True
    )
    
    password = Column(
        String(500),
        nullable=False
    )

    user_demographic: Mapped["models.UserDemographic"] \
        = relationship('UserDemographic', back_populates="user")

    trainer_profile: Mapped["models.TrainerProfile"] \
        = relationship('TrainerProfile', back_populates="user")


    # models.Tr
    # trainer_profile: Mapped["models.TrainerProfile"] \
    #     = relationship(back_populates="user")
    
    # exercises: Mapped[List[models.Exercise]] \
    #     = relationship()