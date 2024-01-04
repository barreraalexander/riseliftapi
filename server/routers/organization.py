from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError


router = APIRouter(
    prefix="/organization",
    tags=['organization'],
)


@router.post(
    "/",
    status_code = status.HTTP_201_CREATED,
    response_model = schemas.OrganizationOut
)
def create(
    create_schema: schemas.OrganizationCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):    
    new_model = models.Organization(
        owner_xid = current_user.xid,
        **create_schema.model_dump()
    )

    try:
        db.add(new_model)
        db.commit()
        db.refresh(new_model)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
        )

    return new_model


@router.get(
    '/',
    response_model = List[schemas.OrganizationOut]
)
def get_all(
    db: Session = Depends(get_db)
):
    db_models = db \
        .query(models.Organization) \
        .all()

    return db_models


@router.get(
    '/{id}',
    response_model = schemas.OrganizationOut
)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    model = db \
        .query(models.Organization)\
        .filter(models.Organization.xid == id) \
        .first()
    
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )


    if model.owner_xid!=current_user.xid:
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
        .query(models.Organization)\
        .filter(models.Organization.xid == id)

    model = query.first()

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )

    if model.owner_xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )

    query.delete(synchronize_session=False)    
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put(
    "/{id}",
    response_model=schemas.OrganizationOut
)
def update(
    id: int,
    update_schema: schemas.OrganizationUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    query = db \
        .query(models.Organization)\
        .filter(models.Organization.xid == id)

    model = query.first()

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        ) 

    if model.owner_xid!=current_user.xid:
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