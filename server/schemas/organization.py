from pydantic import BaseModel, constr
from typing import Optional

class OrganizationBase(BaseModel):
    xid: int
    
class OrganizationColumns(BaseModel):
    name: constr(max_length=255)
    display_name: Optional[constr(max_length=255)]

class OrganizationColumnsOptional(BaseModel):
    name: Optional[constr(max_length=255)] = None
    display_name: Optional[constr(max_length=255)] = None

class OrganizationCreate(OrganizationColumns):
    pass

class OrganizationUpdate(
    # OrganizationBase,
    OrganizationColumnsOptional
):
    pass

class OrganizationOut(
    OrganizationBase,
    OrganizationColumns
):
    pass

