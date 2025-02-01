from server.database import Base
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone


class Mixin(object):
    upldate = Column(
        DateTime,
        nullable=False,
        default=datetime.now(timezone.utc)
    )
    
    moddate = Column(
        DateTime,
        nullable=False,
        default=datetime.now(timezone.utc)
    )
