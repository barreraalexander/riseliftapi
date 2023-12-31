from server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from server import models
# from server.models.user import User

from .mixins.upldate_moddate import Mixin as time_mixin

class UserDemographic(Base, time_mixin):
    
    __tablename__ = 'user_demographic'
    
    xid = Column(
        Integer,
        primary_key=True,
        nullable=False
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

    user_xid: Mapped[int] \
        = mapped_column(
            ForeignKey("user.xid"),
            nullable=False
        )

    user: Mapped["models.User"] \
        = relationship(
            'User',
            foreign_keys=[user_xid],
            back_populates="user_demographic",
            single_parent=True
        )
    