from server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .mixins.upldate_moddate import Mixin as time_mixin

class UserDemographic(Base, time_mixin):
    
    __tablename__ = 'user_demographic'
    
    user_demographic_id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    user_id = Column(
        Integer,
        ForeignKey("user.user_id"),
        nullable=False,
        unique=True,
    )
    
    # cm
    height_inch = Column(
        Integer,
        nullable=True
    )

    # grams
    weight_gram = Column(
        Integer,
        nullable=True
    )

    activity_level = Column(
        Integer,
        nullable=True
    )

    goal = Column(
        Integer,
        nullable=True
    )

    weight_goal = Column(
        Integer,
        nullable=True
    )
