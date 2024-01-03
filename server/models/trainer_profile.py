from server.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from server import models
from .mixins.upldate_moddate import Mixin as time_mixin

class TrainerProfile(Base, time_mixin):
    __tablename__ = 'trainer_profile'

    # it seems this column has to be mapped
    xid = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    # maybe 'override' doesn't need to be included
    override_display_name = Column(
        String(255),
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
            # back_populates="user_demographic",
            single_parent=True
        )

    organization_xid: Mapped[int] \
        = mapped_column(
            ForeignKey("organization.xid"),
            nullable=False
        )
    
    # organization: Mapped["models.Organization"] \
    #     = relationship(
    #         'Organization',
    #         foreign_keys=[organization_xid],
    #         # back_populates="user_demographic",
    #         single_parent=True
    #     )
    


    