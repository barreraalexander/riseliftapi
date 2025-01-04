from pydantic import BaseModel, constr
from enum import IntEnum
from typing import Optional, List
from datetime import datetime


class BaseWorkoutSession(BaseModel):
    xid: int

class WorkoutSessionColumns(
    BaseModel
):
    user_xid: int
    name: Optional[str] = None
    start_time_utc: Optional[datetime] = None
    end_time_utc: Optional[datetime] = None
    deleted_utc: Optional[datetime] = None


class WorkoutSessionColumnsOptional(
    BaseModel
):
    user_xid: Optional[int]
    name: Optional[str] = None
    start_time_utc: Optional[datetime] = None
    end_time_utc: Optional[datetime] = None
    deleted_utc: Optional[datetime] = None



class WorkoutSessionCreate(
    WorkoutSessionColumns
):
    user_xid: Optional[int] = None



class WorkoutSessionUpdate(
    WorkoutSessionColumnsOptional
):
    end_workout: Optional[bool] = None
    user_xid: Optional[int] = None


class WorkoutSessionOut(
    BaseWorkoutSession,
    WorkoutSessionColumns
):
    pass


class WorkoutSession(
    BaseWorkoutSession,
    WorkoutSessionColumns
):
    pass