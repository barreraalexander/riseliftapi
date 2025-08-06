from pydantic import BaseModel, StringConstraints
from enum import IntEnum
from typing import Optional, List
from typing_extensions import Annotated

from datetime import datetime

from .workout_routine import WorkoutRoutine


class TargetMuscleOption(BaseModel):
    value: str
    label: str
    

class UserDashboardConstData(
    BaseModel
):
    pass
    # targetMuscles: Optional[List[str]] = None
    # targetMuscleOptions: Optional[List[TargetMuscleOption]] = None

    
class WorkoutRoutineConstData(
    BaseModel
):
    target_muscle_options: Optional[List[TargetMuscleOption]] = None
    user_workout_routines: Optional[List[WorkoutRoutine]] = None

    
class LandingConstData(
    BaseModel
):
    product_name: str = "Uprise"
    product_subtitle: str = "Weight Lifting Tracker and Hypertrophy coach"
    
