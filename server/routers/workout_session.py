from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone


router = APIRouter(
    prefix="/workout_session",
    tags=['WorkoutSession'],
)

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.WorkoutSession
)
def create(
    create_schema: schemas.WorkoutSessionCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    current_user: models.User = current_user
    
    create_schema.user_xid = current_user.xid

    create_schema.start_time_utc = datetime.now(timezone.utc)



    new_model = models.WorkoutSession(
        **create_schema.model_dump()
    )


    try:
        db.add(new_model)
        db.commit()
        db.refresh(new_model)
    except IntegrityError:
        db.rollback()

    return new_model



@router.get(
    '/',
    response_model=List[schemas.WorkoutSessionOut]
)
def get_all(
    db: Session = Depends(get_db),
    current_user: schemas.WorkoutSessionOut = Depends(oauth2.get_current_user)

):
    current_user: models.User = current_user

    all_models = db\
        .query(models.WorkoutSession)\
        .filter(models.WorkoutSession.user_xid==current_user.xid)\
        .order_by(models.WorkoutSession.name)\
        .all()

    return all_models


@router.put(
    "/{id}",
    response_model=schemas.WorkoutSessionOut,
)
def update(
    id: int,
    update_schema: schemas.WorkoutSessionUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    query = db \
        .query(models.WorkoutSession)\
        .filter(models.WorkoutSession.xid == id)

    model = query.first()

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        ) 

    if model.user_xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )

    if (update_schema.end_workout):
        update_schema.end_time_utc = datetime.now(timezone.utc)
    
    
    # need to add moddates here
    # update_schema.end_time_utc = datetime.now(timezone.utc)
    

    query.update(
        update_schema.model_dump(exclude_none=True, exclude={"end_workout"}),
        synchronize_session=False
    )

    db.commit()

    return query.first()
