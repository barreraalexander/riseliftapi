from pydantic import BaseModel, StringConstraints
from enum import IntEnum
from typing import Optional, List, Literal
from typing_extensions import Annotated

from datetime import datetime


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

class CommonMuscle(BaseModel):
    muscles_targeted: List[TargetMuscles] = []
    display_name: str

class CommonMuscleGroups(BaseModel):
    pectorals: CommonMuscle = CommonMuscle(
        display_name="Pecs"
    )

    lats: CommonMuscle = CommonMuscle(
        display_name="Lats"
    )

    dorsals: CommonMuscle = CommonMuscle(
        display_name="Dorsals"
    )
    
    quadriceps: CommonMuscle = CommonMuscle(
        display_name="Quads"
    )
 
    hamstrings: CommonMuscle = CommonMuscle(
        display_name="Hamstrings"
    )


    glutes: CommonMuscle = CommonMuscle(
        display_name="Glutes"
    )

    calves: CommonMuscle = CommonMuscle(
        display_name="Calves"
    )

    deltoids: CommonMuscle = CommonMuscle(
        display_name="Delts"
    )

    biceps: CommonMuscle = CommonMuscle(
        display_name="Biceps"
    )

    triceps: CommonMuscle = CommonMuscle(
        display_name="Triceps"
    )

    abdominals: CommonMuscle = CommonMuscle(
        display_name="Abs"
    )

    traps: CommonMuscle = CommonMuscle(
        display_name="Traps"
    )


    obliques: CommonMuscle = CommonMuscle(
        display_name="Obliques"
    )




class SimpleMuscleGroups(BaseModel):
    arms: List[int] = []
    legs: List[int] = []
    back: List[int] = []
    chest: List[int] = []
    core: List[int] = []    


# what is going to be the best way to handle this grouping? 
# what i want is a dict like 

class BaseExercise(BaseModel):
    xid: int

class BaseExerciseUser(BaseModel):
    user_xid: int


class ExerciseColumns(
    BaseModel
):
    user_xid: Optional[int] = None

    name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None
    common_muscle_group_target: Optional[str] = None
    # target_muscles_json: Optional[str] = None
    deleted: Optional[datetime] = None

class ExerciseColumnsOptional(
    BaseModel
):
    user_xid: Optional[int] = None
    common_muscle_group_target: Optional[str] = None
    name: Optional[Annotated['str', StringConstraints(max_length=255)]] = None
    target_muscles_json: Optional[str] = None
    deleted: Optional[datetime] = None

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


