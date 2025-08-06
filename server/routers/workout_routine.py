# from fastapi import APIRouter, status, HTTPException, Depends, Response
# from server import schemas, models, oauth2
# from server.database import get_db
# from sqlalchemy.orm import Session
# from typing import List
# from sqlalchemy.exc import IntegrityError
# from datetime import datetime, timezone
# from sqlalchemy import desc


# router = APIRouter(
#     prefix="/workout_routine_exercise_relationship",
#     tags=['Workout Routine Exercise Relationship'],
# )


# @router.post(
#     "/",
#     status_code=status.HTTP_201_CREATED,
#     response_model=schemas.WorkoutRoutineExerciseRelationshipOut
# )
# def create(
#     create_schema: schemas.WorkoutRoutineExerciseRelationship,
#     db: Session = Depends(get_db),
#     current_user: schemas.UserOut = Depends(oauth2.get_current_user)
# ):
#     current_user: models.User = current_user
    
#     create_schema.user_xid = current_user.xid



#     new_model = models.Exercise(
#         **create_schema.model_dump()
#     )


#     try:
#         db.add(new_model)
#         db.commit()
#         db.refresh(new_model)
#     except IntegrityError:
#         db.rollback()

#     return new_model
