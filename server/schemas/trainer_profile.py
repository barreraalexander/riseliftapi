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
    BaseTrainerProfileOrganization,
):
    override_display_name: Optional[constr(max_length=255)] = None

class TrainerProfileColumnsOptional(BaseModel):
    user_xid: Optional[int] = None
    organization_xid: Optional[int] = None
    override_display_name: Optional[constr(max_length=255)] = None

class TrainerProfileCreate(
    TrainerProfileColumns,
):
    pass

class TrainerProfileUpdate(
    # BaseModel
    # BaseTrainerProfile,
    TrainerProfileColumnsOptional,
):
    xid: Optional[int] = None

    pass


class TrainerProfileOut(
    BaseTrainerProfile,
    BaseTrainerProfileUser,
    TrainerProfileColumns,
    # TrainerProfile,
    # BaseTrainerProfileUser
):

    moddate: datetime
    upldate: datetime


# class TrainerProfileOutwithRelationships(
#     BaseTrainerProfile,
#     BaseTrainerProfileUser,
#     TrainerProfileColumns,
#     # TrainerProfile,
#     # BaseTrainerProfileUser
# ):

#     moddate: datetime
#     upldate: datetime


class TrainerProfile(
    BaseTrainerProfile,
    # BaseTrainerProfileUser,
    # BaseTrainerProfileOrganization,
    TrainerProfileColumns
):
    pass

