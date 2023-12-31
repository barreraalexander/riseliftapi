from pydantic import BaseModel, constr
from typing import Optional

class TrainerProfileBase(BaseModel):
    trainer_profilexid: int

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


class TrainerProfile(
    TrainerProfileBase,
    TrainerProfileColumns
):
    pass