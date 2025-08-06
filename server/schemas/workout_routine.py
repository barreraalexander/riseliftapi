from pydantic import BaseModel, StringConstraints, field_serializer
from enum import IntEnum
from typing import Optional, List, Literal
from typing_extensions import Annotated

from .workout_routine_exercise_relationship import WorkoutRoutineExerciseRelationship

class WorkoutRoutineDays(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class BaseWorkoutRoutine(BaseModel):
    xid: int

class BaseWorkoutRoutineUser(BaseModel):
    user_xid: int



class WorkoutRoutineColumns(
    BaseWorkoutRoutineUser
):
    name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None
    day: WorkoutRoutineDays
    is_rest_day: bool = False

class WorkoutRoutineColumnsOptional(
    BaseWorkoutRoutineUser
):
    name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None
    day: Optional[WorkoutRoutineDays] = None
    is_rest_day: Optional[bool] = None


class WorkoutRoutineCreate(
    WorkoutRoutineColumns
):
    pass 

class WorkoutRoutineUpdate(
    WorkoutRoutineColumnsOptional
):
    pass

class WorkoutRoutineOut(
    BaseWorkoutRoutine,
    WorkoutRoutineColumns
):
    pass

class WorkoutRoutine(
    BaseWorkoutRoutine,
    WorkoutRoutineColumns
):
    exercise_relationships: List[WorkoutRoutineExerciseRelationship] = []
    
    @field_serializer("day")
    def serialize_day(self, day: WorkoutRoutineDays):
        return day.name

    pass