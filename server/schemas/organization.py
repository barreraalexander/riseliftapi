from pydantic import BaseModel, constr
from typing import Optional

class OrganizationBase(BaseModel):
    organizationxid: int
    
class OrganizationColumns(BaseModel):
    name: constr(max_length=255)
    display_name: Optional[constr(max_length=255)]

class OrganizationColumnsOptional(BaseModel):
    name: Optional[constr(max_length=255)]
    display_name: Optional[constr(max_length=255)]

class OrganizationCreate(OrganizationColumns):
    pass

class OrganizationUpdate(
    OrganizationBase,
    OrganizationColumnsOptional
):
    pass

