from pydantic import BaseModel, StringConstraints
from typing import Optional
from typing_extensions import Annotated


from .mixins.upldate_moddate import UpldateModdateCreate, UpldateModdateOut, UpldateModdateUpdate


class OrganizationBase(BaseModel):
    xid: int
    
class OrganizationColumns(BaseModel):
    name: Annotated['str', StringConstraints(max_length=255)]
    display_name: Optional[Annotated['str', StringConstraints(max_length=255)]]

class OrganizationColumnsOptional(BaseModel):
    name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None
    display_name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None

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

