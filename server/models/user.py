from server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    upldate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    moddate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
