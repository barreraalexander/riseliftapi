from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/exercise",
    tags=['Exercise'],
)

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Exercise
)
def create(
    create_schema: schemas.ExerciseCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    current_user: models.User = current_user
    
    new_model = models.Exercise(
        **create_schema.model_dump()
    )

    db.add(new_model)

    try:
        db.commit()
        db.refresh(new_model)
    except IntegrityError:
        db.rollback()

    return new_model


@router.get(
    '/',
    response_model=List[schemas.Exercise]
)
def get_all(
    db: Session = Depends(get_db)
):
    models = db.query(models.Exercise)\
        .all()

    return models


@router.get(
    '/{id}',
    response_model=schemas.Exercise
)
def get_byxid(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    model = db.query(models.Exercise)\
        .filter(
            models.Exercise.xid == id
        ).first()
   
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Model not found'
        )


    if model.xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    return model

@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    
    model_query = db.query(models.Exercise)\
        .filter(models.Exercise.xid == id)

    model: models.Exercise = model_query.first()

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model was not found"
        )

    if model.xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    model_query.delete(synchronize_session=False)

    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
