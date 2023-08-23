from server.database import Base
from sqlalchemy import Column, DateTime
from datetime import datetime


class Mixin(object):
    upldate = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    
    moddate = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )
