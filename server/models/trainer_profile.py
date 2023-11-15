from server.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from server import models
from .mixins.upldate_moddate import Mixin as time_mixin

class TrainerProfile(Base, time_mixin):
    __tablename__ = 'trainer_profile'

    # it seems this column has to be mapped
    trainer_profile_id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    # maybe 'override' doesn't need to be included
    override_display_name = Column(
        String(255),
        nullable=True
    )

    user_id: Mapped[int] \
        = mapped_column(
            ForeignKey("user.user_id"),
            nullable=False
        )

    user: Mapped["models.User"] \
        = relationship(back_populates="trainer_profile")
    
    organization_id: Mapped[int] \
        = mapped_column(
            ForeignKey("organization.organization_id")
        )

    organization: Mapped["models.Organization"] \
        = relationship(back_populates="trainer_profile")
    

    