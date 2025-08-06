from pydantic import BaseModel
from typing import Optional

from .exercise import Exercise


class BaseWorkoutRoutineExerciseRelationship(BaseModel):
    xid: int

class WorkoutRoutineExerciseRelationshipColumns(
    BaseModel
):
    workout_routine_xid: int
    exercise_xid: Optional[int] = None


class WorkoutRoutineExerciseRelationshipColumnsOptional(
    BaseModel
):
    workout_routine_xid: Optional[int] = None
    exercise_xid: Optional[int] = None


class WorkoutRoutineExerciseRelationshipCreate(
    WorkoutRoutineExerciseRelationshipColumns
):
    pass 

class WorkoutRoutineExerciseRelationshipUpdate(
    WorkoutRoutineExerciseRelationshipColumnsOptional
):
    pass

class WorkoutRoutineExerciseRelationshipOut(
    BaseWorkoutRoutineExerciseRelationship,
    WorkoutRoutineExerciseRelationshipColumns
):
    pass

class WorkoutRoutineExerciseRelationship(
    BaseWorkoutRoutineExerciseRelationship,
    WorkoutRoutineExerciseRelationshipColumns
):
    exercise: Optional[Exercise] = None
