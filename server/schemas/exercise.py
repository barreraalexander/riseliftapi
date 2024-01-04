from pydantic import BaseModel, constr
from enum import IntEnum
from typing import Optional, List


class TargetMuscles(IntEnum):
    # chest
    pectoralis_major = 0
    # traps
    trapezius = 5
    # abs
    external_oblique = 6
    internal_oblique = 7
    rectus_abdominis = 8
    transverse_abdominis = 9
    # shoulders
    anterior_deltoid = 10
    lateral_deltoid = 10
    posterior_deltoid = 10
    # arms
    biceps_brachii = 11
    triceps_brachii = 12
    brachioradialis = 13
    latissimus_dorsi = 14
    musculi_dorsi = 15
    # 3 muscles for hamstrings
    semitendinosus = 16
    semimembranosus = 17
    biceps_femoris = 18
    # 3 muscles for calves
    gastrocnemius = 19
    tibilias_anterior = 20
    soleus = 21
    # 4 muscles for quads
    sartorius = 22
    rectus_femoris = 23
    vastus_lateralis = 24
    vastus_medialis = 25

class MuscleTargetLevels(IntEnum):
    primary = 0
    secondary = 1
    tertiary = 2


class CommonMuscleGroups(BaseModel):
    hamstrings: List[int] = []
    pectorals: List[int] = []
    quadriceps: List[int] = []
    deltoids: List[int] = []

class SimpleMuscleGroups(BaseModel):
    arms: List[int] = []
    legs: List[int] = []
    back: List[int] = []
    chest: List[int] = []
    core: List[int] = []    


class BaseExercise(BaseModel):
    xid: int

class BaseExerciseUser(BaseModel):
    user_xid: int


class ExerciseColumns(
    BaseModel
):
    name: constr(max_length=255)
    target_muscles_json: Optional[str] = None

class ExerciseColumnsOptional(
    BaseModel
):
    user_xid: Optional[int] = None
    name: Optional[constr(max_length=255)] = None
    target_muscles_json: Optional[str] = None

class ExerciseCreate(
    ExerciseColumns
):
    pass

class ExerciseUpdate(
    ExerciseColumnsOptional
):
    pass

class ExerciseOut(
    BaseExercise,
    ExerciseColumns
):
    pass

class Exercise(
    BaseExercise,
    ExerciseColumns
):
    target_muscles: dict[int, List[int]] = {}


