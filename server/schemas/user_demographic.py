from pydantic import BaseModel
from typing import Optional
from enum import IntEnum
from datetime import datetime

class UserGoalEnum(IntEnum):
    UNSET = 0
    CARDIO = 1
    STRENGTH = 2
    STAMINA = 3
    FLEXIBILITY = 4
    HEALTHY = 5

class ActivityLevelEnum(IntEnum):
    UNSET = 0
    SEDENTARY = 1
    LIGHT = 2
    MODERATE = 3
    HEAVY = 4


class BaseUserDemographic(BaseModel):
    xid: int

class BaseUserDemographicUser(BaseModel):
    user_xid: int

# what about user_id?
class UserDemographicColumnsOptional(BaseModel):
    height_inch: Optional[int] = None
    
    weight_gram: Optional[int] = None

    activity_level: Optional[ActivityLevelEnum] = None
    goal: Optional[UserGoalEnum] = None

    weight_goal: Optional[int] = None


# What about user_id?
class UserDemographicColumnsOptional(BaseModel):
    height_inch: Optional[int] = None

    weight_gram: Optional[int] = None

    activity_level: Optional[ActivityLevelEnum] = None
    goal: Optional[UserGoalEnum] = None

    weight_goal: Optional[int] = None

class UserDemographicCreate(
    UserDemographicColumnsOptional
):
    pass

class UserDemographic(
    BaseUserDemographic,
    BaseUserDemographicUser,
    UserDemographicColumnsOptional
):
    pass

class UserDemographicOut(
    UserDemographic
):
# class UserDemographicOut(
#     BaseUserDemographic,
#     BaseUserDemographicUser,
#     UserDemographicColumnsOptional
# ):
    moddate: datetime
    upldate: datetime

class UserDemographicUpdate(
    UserDemographicColumnsOptional,
):
    moddate: datetime = datetime.utcnow()