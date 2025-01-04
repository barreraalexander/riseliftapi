from pydantic import BaseModel, StringConstraints
from typing import Optional
from typing_extensions import Annotated

from datetime import datetime

from .mixins.upldate_moddate import UpldateModdateCreate, UpldateModdateOut, UpldateModdateUpdate


class BaseTrainerProfile(BaseModel):
    xid: int

class BaseTrainerProfileUser(BaseModel):
    user_xid: int

class BaseTrainerProfileOrganization(BaseModel):
    organization_xid: int


class TrainerProfileColumns(
    BaseTrainerProfileOrganization,
):
    override_display_name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None

class TrainerProfileColumnsOptional(BaseModel):
    user_xid: Optional[int] = None
    organization_xid: Optional[int] = None
    override_display_name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None

class TrainerProfileCreate(
    TrainerProfileColumns,
    UpldateModdateCreate
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
    UpldateModdateOut
    # TrainerProfile,
    # BaseTrainerProfileUser
):
    pass


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

