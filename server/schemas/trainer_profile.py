from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime

class BaseTrainerProfile(BaseModel):
    xid: int

class BaseTrainerProfileUser(BaseModel):
    user_xid: int

class BaseTrainerProfileOrganization(BaseModel):
    organization_xid: int


class TrainerProfileColumns(
    # BaseModel,
    BaseTrainerProfileOrganization,
    BaseTrainerProfileUser,
    ):
    override_display_name: Optional[constr(max_length=255)] = None

class TrainerProfileColumnsOptional(BaseModel):
    user_xid: Optional[int]
    organization_xid: Optional[int]
    override_display_name: Optional[constr(max_length=255)]

class TrainerProfileCreate(
    # BaseTrainerProfileUser,
    TrainerProfileColumns,
    # BaseTrainerProfileOrganization
):
    pass

class TrainerProfileUpdate(
    BaseTrainerProfile,
    TrainerProfileColumnsOptional,
):
    pass


class TrainerProfileOut(
    BaseTrainerProfile,
    TrainerProfileColumns,
    # TrainerProfile,
    # BaseTrainerProfileUser
):

    moddate: datetime
    upldate: datetime


class TrainerProfile(
    BaseTrainerProfile,
    # BaseTrainerProfileUser,
    # BaseTrainerProfileOrganization,
    TrainerProfileColumns
):
    pass

