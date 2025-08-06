from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone
from sqlalchemy import desc


router = APIRouter(
    prefix="/workout_routine_exercise_relationship",
    tags=['Workout Routine Exercise Relationship'],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.WorkoutRoutine
)
def create(
    create_schema: schemas.WorkoutRoutineExerciseRelationshipCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    current_user: models.User = current_user
    
    # create_schema.user_xid = current_user.xid



    new_model = models.WorkoutRoutineExerciseRelationship(
        **create_schema.model_dump()
    )


    try:
        db.add(new_model)
        db.commit()
        db.refresh(new_model)
    except IntegrityError:
        db.rollback()

    updated_workout_routine = db \
        .query(models.WorkoutRoutine) \
        .filter(models.WorkoutRoutine.xid==create_schema.workout_routine_xid)\
        .first()

    updated_workout_routine_schema = schemas.WorkoutRoutine(
        **updated_workout_routine.__dict__,
        exercise_relationships=[
            schemas.WorkoutRoutineExerciseRelationship(
                **exercise_relationship.__dict__,
                exercise=schemas.Exercise(**exercise_relationship.exercise.__dict__) if exercise_relationship.exercise else None
                # exercise=schemas.Exercise(**exercise_relationship.exercise.__dict__) or None
            ) 
            for exercise_relationship
            in updated_workout_routine.exercise_relationships
        ]
    )

    return updated_workout_routine_schema

@router.put(
    "/{id}",
    response_model=schemas.WorkoutRoutine,
)
def update(
    id: int,
    update_schema: schemas.WorkoutRoutineExerciseRelationshipUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    query = db \
        .query(models.WorkoutRoutineExerciseRelationship)\
        .filter(models.WorkoutRoutineExerciseRelationship.xid == id)

    model = query.first()



    if model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        ) 

    query.update(
        update_schema.model_dump(exclude_none=True),
        synchronize_session=False
    )

    db.commit()


    updated_workout_routine = db \
        .query(models.WorkoutRoutine) \
        .filter(models.WorkoutRoutine.xid==model.workout_routine_xid)\
        .first()

    updated_workout_routine_schema = schemas.WorkoutRoutine(
        **updated_workout_routine.__dict__,
        exercise_relationships=[
            schemas.WorkoutRoutineExerciseRelationship(
                **exercise_relationship.__dict__,
                exercise=schemas.Exercise(**exercise_relationship.exercise.__dict__) if exercise_relationship.exercise else None
            ) 
            for exercise_relationship
            in updated_workout_routine.exercise_relationships
        ]
    )

    return updated_workout_routine_schema



    # return query.first()