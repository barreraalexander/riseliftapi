from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
from sys import getsizeof


router = APIRouter(
    prefix="/organization",
    tags=['organization'],
)



@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.OrganizationOut
)
def create_organization(
    create_schema: schemas.OrganizationCreate,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):    
    new_model = models.Organization(
        owner_xid = current_user.xid,
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
            detail=f"Organization for User {current_user.xid} already exists. Not authorized to perform requested action. Error: {str(e._message)}"
        )

    return new_model

@router.get(
    '/',
    response_model=List[schemas.OrganizationOut]
)
def get_organizations(
    db: Session = Depends(get_db)
):
    db_models = db.query(models.Organization).all()

    return db_models

@router.get(
    '/{id}',
    response_model=schemas.OrganizationOut
)
def get_organization(
    id: int,
    db: Session = Depends(get_db),
    current_user: int=Depends(oauth2.get_current_user)
):
    model = db.query(models.UserDemographic)\
        .filter(models.UserDemographic.xid == id).first()
    
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User Demographic not found'
        )


    if model.userxid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    return model