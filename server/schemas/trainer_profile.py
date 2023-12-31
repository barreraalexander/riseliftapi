from pydantic import BaseModel, constr
from typing import Optional

class BaseTrainerProfile(BaseModel):
    xid: int

class BaseTrainerProfileUser(BaseModel):
    user_xid: int


class TrainerProfileColumns(BaseModel):
    override_display_name: Optional[constr(max_length=255)]

class TrainerProfileColumnsOptional(BaseModel):
    user_xid: Optional[int]
    override_display_name: Optional[constr(max_length=255)]

class TrainerProfileCreate(
    BaseTrainerProfileUser,
    TrainerProfileColumns
):
    pass

class TrainerProfileUpdate(
    BaseTrainerProfile,
    TrainerProfileColumnsOptional,
):
    pass


class TrainerProfile(
    BaseTrainerProfile,
    BaseTrainerProfileUser,
    TrainerProfileColumns
):
    pass

class TrainerProfileOut(
    TrainerProfile,
):
    pass