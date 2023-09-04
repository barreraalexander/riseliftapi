from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from server.utils import hash
# from pymysql.err import IntegrityError
from sqlalchemy.exc import IntegrityError

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
    user_demographic: schemas.UserDemographicCreate,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):    
    new_user_demographic = models.UserDemographic(
        user_id = current_user.user_id,
        **user_demographic.model_dump()
    )

    # need to do a unique check here


    db.add(new_user_demographic)

    try:
        db.commit()
        db.refresh(new_user_demographic)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"User Demographic object for User {current_user.user_id} already exists. Not authorized to perform requested action"
        )

    return new_user_demographic


@router.get(
    '/',
    response_model=List[schemas.UserDemographicOut]
)
def get_user_demographics(
    db: Session = Depends(get_db)
):
    get_user_demographics = db.query(models.UserDemographic).all()

    return get_user_demographics


@router.get(
    '/{id}',
    response_model=schemas.UserDemographicOut
)
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):
    user_demographic = db.query(models.UserDemographic)\
        .filter(models.UserDemographic.user_demographic_id == id).first()
   
    if not user_demographic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User Demographic not found'
        )


    if user_demographic.user_id!=current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    return user_demographic



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

    if user_demographic.user_id!=current_user.user_id:
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
        .filter(models.UserDemographic.user_demographic_id == id)

    user_demographic = user_demographic_query.first()

    if user_demographic==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Demographic was not found"
        ) 

    if user_demographic.user_id!=current_user.user_id:
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