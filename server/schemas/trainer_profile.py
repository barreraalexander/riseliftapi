from pydantic import BaseModel, constr
from typing import Optional

class TrainerProfileBase(BaseModel):
    trainer_profile_id: int

class TrainerProfileColumns(BaseModel):
    pass

class TrainerProfileColumnsOptional(BaseModel):
    pass

class TrainerProfileCreate(TrainerProfileColumns):
    pass

class TrainerProfileUpdate(
    TrainerProfileBase,
    TrainerProfileColumnsOptional
):
    pass

