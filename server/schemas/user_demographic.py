from pydantic import BaseModel, constr
from typing import Optional
from enum import IntEnum

class UserGoalEnum(IntEnum):
    CARDIO = 0
    STRENGTH = 1
    STAMINA = 2
    FLEXIBILITY = 3
    HEALTHY = 4

class ActivityLevelEnum(IntEnum):
    SEDENTARY = 0
    LIGHT = 1
    MODERATE = 2
    HEAVY = 3


class BaseUserDemographic(BaseModel):
    user_demographic_id: int
    # user_id: int

class BaseUserDemographicUser(BaseModel):
    user_id: int



class UserDemographicColumnsOptional(BaseModel):
    # cm
    height: Optional[int] = None
    
    # grams 
    weight: Optional[int] = None

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
    BaseUserDemographic,
    BaseUserDemographicUser,
    UserDemographicColumnsOptional
):
    pass

class UserDemographicUpdate(
    UserDemographicColumnsOptional,
):
    pass