from pydantic import BaseModel, StringConstraints
from typing import Optional
from typing_extensions import Annotated

from .user_demographic import UserDemographic
from .trainer_profile import TrainerProfile
from .mixins.upldate_moddate import UpldateModdateCreate, UpldateModdateOut, UpldateModdateUpdate

class BaseUser(BaseModel):
    xid: int

class BaseUserPassword(BaseModel):
    password: Annotated['str', StringConstraints(max_length=500)]

class UserNames(BaseModel):
    
    first_name: Optional[Annotated['str', StringConstraints(max_length=255)]]
    last_name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None
    display_name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None

class UserNamesOptional(BaseModel):
    first_name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None
    last_name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None
    display_name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None

class UserColumns(UserNames):
    email: Annotated['str', StringConstraints(max_length=255)]


class UserColumnsOptional(
    UserNames
):
    email: Optional[Annotated['str', StringConstraints(max_length=255)]] = None

class UserOut(
    BaseUser,
    UserColumns,
    UpldateModdateOut
):
    pass


class UserOutwithRelationships(
    BaseUser,
    UserColumns
):
    user_demographic: Optional[UserDemographic]
    trainer_profile: Optional[TrainerProfile]


class UserOutAll(
    UserOut,
    BaseUserPassword
):
    pass

class UserCreate(
    UserColumns,
    BaseUserPassword,
    UpldateModdateCreate
):
    pass
    
class UserUpdate(
    UserColumnsOptional,
    UpldateModdateUpdate
):
    pass
