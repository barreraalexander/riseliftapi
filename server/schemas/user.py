from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime

from .user_demographic import UserDemographic
from .trainer_profile import TrainerProfile

class BaseUser(BaseModel):
    xid: int

class BaseUserPassword(BaseModel):
    password: constr(max_length=500)

class UserNames(BaseModel):
    first_name: constr(max_length=255)
    last_name: Optional[constr(max_length=255)] = None
    display_name: Optional[constr(max_length=255)] = None

class UserNamesOptional(BaseModel):
    first_name: Optional[constr(max_length=255)] = None
    last_name: Optional[constr(max_length=255)] = None
    display_name: Optional[constr(max_length=255)] = None

class UserColumns(UserNames):
    email: constr(max_length=255)


class UserColumnsOptional(UserNames):
    email: Optional[constr(max_length=255)] = None

class UserOut(BaseUser, UserColumns):
    moddate: datetime
    upldate: datetime

# class UserOut(BaseUser, UserColumns):
#     moddate: datetime
#     upldate: datetime

class UserOutwithRelationships(BaseUser, UserColumns):
    user_demographic: Optional[UserDemographic]
    trainer_profile: Optional[TrainerProfile]


class UserOutAll(UserOut, BaseUserPassword):
    pass

class UserCreate(UserColumns, BaseUserPassword):
    moddate: datetime = datetime.utcnow()
    upldate: datetime = datetime.utcnow()
    
class UserUpdate(UserColumnsOptional):
    moddate: datetime = datetime.utcnow()