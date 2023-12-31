from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from server.utils import hash


router = APIRouter(
    prefix="/user",
    tags=['User'],
)

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut
)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):    
    hashed_password = hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get(
    '/',
    response_model=List[schemas.UserOut]
)
def get_users(
    db: Session = Depends(get_db)
):
    user = db.query(models.User).all()

    return user


@router.get(
    '/fullusers',
    response_model=List[schemas.UserOutAll]
)
def get_users_full(
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):
    user = db.query(models.User).all()

    return user



@router.get(
    '/{id}',
    response_model=schemas.UserOut
)
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')


    if user.user_id!=current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    return user



@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):
    
    user_query = db.query(models.User).filter(models.User.user_id == id)

    user = user_query.first()

    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    if user.user_id!=current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    user_query.delete(synchronize_session=False)    
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put(
    "/{id}",
    response_model=schemas.UserOut
)
def update_user(
    id: int,
    updated_user: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):
    user_query = db.query(models.User).filter(models.User.user_id == id)

    user = user_query.first()

    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found") 

    if user.user_id!=current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    user_query.update(updated_user.model_dump(exclude_none=True), synchronize_session=False)

    db.commit()

    return user_query.first()