from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime

class BaseUser(BaseModel):
    _id: int

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

class UserOutAll(UserOut, BaseUserPassword):
    pass

class UserCreate(UserColumns, BaseUserPassword):
    pass
    
class UserUpdate(UserColumnsOptional):
    moddate: datetime = datetime.utcnow()