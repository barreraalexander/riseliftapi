from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
from sys import getsizeof


router = APIRouter(
    prefix="/user_demographic",
    tags=['User Demographic'],
)

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserDemographicOut
)
def create_user_demographic(
    create_schema: schemas.UserDemographicCreate,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):    
    new_model = models.UserDemographic(
        user_id = current_user._id,
        **create_schema.model_dump()
    )

    try:
        db.add(new_model)
        db.commit()
        db.refresh(new_model)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User Demographic object for User {current_user._id} already exists. Not authorized to perform requested action. Error: {str(e._message)}"
        )

    return new_model


@router.get(
    '/',
    response_model=List[schemas.UserDemographicOut]
)
def get_user_demographics(
    db: Session = Depends(get_db)
):
    models = db.query(models.UserDemographic).all()

    return models


@router.get(
    '/{id}',
    response_model=schemas.UserDemographicOut
)
def get_user_demographic(
    id: int,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):
    model = db.query(models.UserDemographic)\
        .filter(models.UserDemographic._id == id).first()
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User Demographic not found'
        )


    if model.user_id!=current_user._id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    x = getsizeof(model)

    return model



@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user_demographic(
    id: int,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):
    
    user_demographic_query = db.query(models.UserDemographic)\
        .filter(models.UserDemographic.user_demographic_id == id)

    user_demographic = user_demographic_query.first()

    if user_demographic==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Demographic was not found"
        )

    if user_demographic._id!=current_user._id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    user_demographic_query.delete(synchronize_session=False)

    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put(
    "/{id}",
    response_model=schemas.UserDemographicOut,
)
def update_user_demographic(
    id: int,
    updated_user_demographic: schemas.UserDemographicUpdate,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):
    user_demographic_query = db.query(models.UserDemographic)\
        .filter(models.UserDemographic._id == id)

    user_demographic = user_demographic_query.first()

    if user_demographic==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Demographic was not found"
        ) 

    if user_demographic.user_id!=current_user._id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    user_demographic_query.update(
        updated_user_demographic.model_dump(exclude_none=True),
        synchronize_session=False
    )

    db.commit()

    return user_demographic_query.first()