from pydantic import BaseModel, constr
from typing import Optional

class BaseUser(BaseModel):
    user_id: int

class BaseUserPassword(BaseModel):
    password: constr(max_length=500)

class UserNames(BaseModel):
    first_name: constr(max_length=255)
    last_name: Optional[constr(max_length=255)] = None
    display_name: Optional[constr(max_length=255)] = None

class UserColumns(UserNames):
    email: constr(max_length=255)

class UserOut(BaseUser, UserColumns):
    pass

class UserCreate(UserColumns, BaseUserPassword):
    pass
    