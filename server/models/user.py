from server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from datetime import datetime

from .mixins.upldate_moddate import Mixin as time_mixin

# class User(Base):
class User(Base, time_mixin):
    __tablename__ = 'user'

    user_id = Column(
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