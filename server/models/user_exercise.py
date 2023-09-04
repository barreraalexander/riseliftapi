from server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from datetime import datetime

from .mixins.upldate_moddate import Mixin as time_mixin

class UserExercise(Base, time_mixin):
    __tablename__ = 'user_exercise'


# exercises created by users, belongs to individual musles

# exercise_id
# user_id
# target_muscles (list of enums)
# name
# exercise_type? (enum of cardio, weightlifting, *ability to add custom?)


