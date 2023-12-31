from server.database import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from .mixins.upldate_moddate import Mixin as time_mixin

class UserReport(Base, time_mixin):
    
    __tablename__ = 'user_report'
    
    xid = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    schema_type = Column(
        String(255),
        nullable=False
    )


    report_data = Column(
        String(255),
        nullable=False
    )
