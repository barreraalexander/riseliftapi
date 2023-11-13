from pydantic import BaseModel, constr
from enum import IntEnum
from typing import Optional, List


class TargetMuscles(IntEnum):
    muscles = 1

class ExerciseBase(BaseModel):
    exercise_id: int

class ExerciseColumns(BaseModel):
    user_id: Optional[int]
    name: constr(max_length=255)
    target_muscles: List[TargetMuscles] = []

class ExerciseColumnsOptional(BaseModel):
    user_id: Optional[int]
    name: Optional[constr(max_length=255)]
    target_muscles: List[TargetMuscles] = []

class ExerciseCreate(ExerciseColumns):
    pass

class ExerciseUpdate(ExerciseColumnsOptional):
    pass