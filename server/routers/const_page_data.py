
from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone
from sqlalchemy import desc


router = APIRouter(
    prefix="/const_page_data",
    tags=['Const Page Data'],
)


@router.get(
    '/get_workout_routine_const_data',
    response_model=schemas.WorkoutRoutineConstData
)
def get_workout_routine_const_data(
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)

):
    current_user: models.User = current_user

    
    target_muscle_options: List[schemas.TargetMuscleOption] = []
    
    for target_muscle in schemas.CommonMuscleGroups():

        target_muscle_option = schemas.TargetMuscleOption(
            value=target_muscle[0],
            label=target_muscle[1].display_name
        )

        target_muscle_options.append(target_muscle_option)

    target_muscle_options = sorted(target_muscle_options, key=lambda target_muscle_option: target_muscle_option.label)

    # now I need to get a users list of routines

    user_workout_routines: List[models.WorkoutRoutine] \
        = db.query(models.WorkoutRoutine)\
            .filter(models.WorkoutRoutine.user_xid==current_user.xid)\
            .order_by(models.WorkoutRoutine.xid)\
            .all()
    
    # if there are none--create them? Or, should I just supply defaults on the FE?
    if (not user_workout_routines):
        
        # user_workout_routines: List[models.WorkoutRoutine]

        for routine_day in schemas.WorkoutRoutineDays:
            new_workout_routine = schemas.WorkoutRoutineCreate(
                user_xid=current_user.xid,
                day=routine_day.value,

            )

            new_model = models.WorkoutRoutine(
                **new_workout_routine.model_dump()
            )

            db.add(new_model)
        db.commit()

        user_workout_routines: List[models.WorkoutRoutine] \
            = db.query(models.WorkoutRoutine)\
                .filter(models.WorkoutRoutine.user_xid==current_user.xid)\
                .order_by(models.WorkoutRoutine.xid)\
                .all()
        

    const_data_schema = schemas.WorkoutRoutineConstData(
        target_muscle_options=target_muscle_options,
        user_workout_routines=[
            schemas.WorkoutRoutine(
                **user_workout_routine.__dict__,
                exercise_relationships=[
                    schemas.WorkoutRoutineExerciseRelationship(
                        **exercise_relationship.__dict__,
                        exercise=schemas.Exercise(**exercise_relationship.exercise.__dict__) if exercise_relationship.exercise else None
                        # exercise=schemas.Exercise(**exercise_relationship.exercise.__dict__) or None
                    ) 
                    for exercise_relationship
                    in user_workout_routine.exercise_relationships
                ]
            )
            for user_workout_routine in user_workout_routines 
        ]

    )

    return const_data_schema

@router.get(
    '/get_user_dashboard_const_data',
    response_model=schemas.UserDashboardConstData
)
def get_user_dashboard_const_data(
    # db: Session = Depends(get_db),
    # current_user: schemas.UserOut = Depends(oauth2.get_current_user)

):
    
    target_muscle_options: List[schemas.TargetMuscleOption] = []
    
    for target_muscle in schemas.CommonMuscleGroups():

        target_muscle_option = schemas.TargetMuscleOption(
            value=target_muscle[0],
            label=target_muscle[1].display_name
        )

        target_muscle_options.append(target_muscle_option)

    target_muscle_options = sorted(target_muscle_options, key=lambda target_muscle_option: target_muscle_option.label)

    

    const_data_schema = schemas.WorkoutRoutineConstData(
        target_muscle_options=target_muscle_options,
        # targetMuscles=target_muscle_options
        # targetMuscles=["Option1", "Option2", "Option3"]
        # targetMuscles=["Option1", "Option2", "Option3"]
    )

    return const_data_schema

@router.get(
    '/get_landing_page_const_data',
    response_model=schemas.UserDashboardConstData
)
def get_landing_page_const_data(
    # db: Session = Depends(get_db),
    # current_user: schemas.UserOut = Depends(oauth2.get_current_user)

):
    
    landing_data_schmea = schemas.LandingConstData()

    return landing_data_schmea