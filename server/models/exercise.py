from server.database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from datetime import datetime

from .mixins.upldate_moddate import Mixin as time_mixin

class Exercise(Base, time_mixin):
    __tablename__ = 'exercise'

    exercise_id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("user.user_id"),
        nullable=True,
    )


    name = Column(
        String(255),
        nullable=False
    )

    # stored as json
    target_muscles = Column(
        Text(),
        nullable=True
    )


    


    # should this be on it's own table?

# if on two tables, the only 


# exercises created by users, belongs to individual musles

# exercise_id
# user_id
# target_muscles (list of enums)
# name
# exercise_type? (enum of cardio, weightlifting, *ability to add custom?)


