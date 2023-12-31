from server.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .mixins.upldate_moddate import Mixin as time_mixin
from typing import List
from server import models
# from models.user import User
# from models.trainer_profile import TrainerProfile

class Organization(Base, time_mixin):
    __tablename__ = 'organization'

    xid: int = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    display_name = Column(
        String(255),
        nullable=True
    )

    owner_xid: Mapped[int] \
        = mapped_column(
            ForeignKey("user.xid")
        )

    owner: Mapped["models.User"] \
        = relationship(
            'User',
            foreign_keys=[owner_xid],
            # back_populates="user_demographic",
            single_parent=True
        )

    # trainer_profiles: Mapped[List["models.TrainerProfile"]] \
    #     = relationship(
    #         'TrainerProfile',
    #         # foreign_keys=[]
    #     )
