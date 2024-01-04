from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from server.utils import hash
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/user",
    tags=['User'],
)


@router.post(
    "/",
    status_code = status.HTTP_201_CREATED,
    response_model = schemas.UserOut
)
def create(
    create_schema: schemas.UserCreate,
    db: Session = Depends(get_db)
):    
    hashed_password = hash(create_schema.password)
    create_schema.password = hashed_password

    new_model = models.User(
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
            detail=f"User email {create_schema.email} is already taken. Error: {str(e._message)}"
        )
    return new_model


@router.get(
    '/',
    response_model=List[schemas.UserOut]
)
def get_all(
    db: Session = Depends(get_db)
):
    db_models = db\
        .query(models.User)\
        .all()

    return db_models


@router.get(
    '/fullusers',
    response_model=List[schemas.UserOutAll]
)
def get_all_full(
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    db_models = db\
        .query(models.User)\
        .all()

    return db_models


@router.get(
    '/{id}',
    response_model=schemas.UserOut
)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    model = db \
        .query(models.User)\
        .filter(models.User.xid == id)\
        .first()
    
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )

    if model.xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return model


@router.get(
    '/with_relationships/{id}',
    response_model=schemas.UserOutwithRelationships
)
def get_by_id_with_relationships(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):

    model = db \
        .query(models.User)\
        .filter(models.User.xid == id)\
        .first()
    
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )

    if model.xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
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
    
    query = db \
        .query(models.User)\
        .filter(models.User.xid == id)

    user = query.first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )

    if user.xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )

    query.delete(synchronize_session=False)    
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put(
    "/{id}",
    response_model=schemas.UserOut
)
def update(
    id: int,
    update_schema: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    query = db \
        .query(models.User)\
        .filter(models.User.xid == id)

    user = query.first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        ) 

    if user.xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )

    query.update(
        update_schema.model_dump(
            exclude_none=True
        ),
        synchronize_session=False
    )

    db.commit()

    return query.first()