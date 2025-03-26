from pydantic import BaseModel, StringConstraints
from enum import IntEnum
from typing import Optional, List
from typing_extensions import Annotated

from datetime import datetime


class UserDashboardConstData(
    BaseModel
):
    targetMuscles: Optional[List[str]] = None
    targetMuscleOptions: Optional[List[str]] = None

    
