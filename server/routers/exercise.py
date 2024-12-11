from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone


router = APIRouter(
    prefix="/exercise",
    tags=['Exercise'],
)

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ExerciseOut
)
def create(
    create_schema: schemas.ExerciseCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    current_user: models.User = current_user
    
    create_schema.user_xid = current_user.xid

    new_model = models.Exercise(
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
    response_model=List[schemas.ExerciseOut]
)
def get_all(
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)

):
    current_user: models.User = current_user

    all_models = db\
        .query(models.Exercise)\
        .filter(models.Exercise.user_xid==current_user.xid)\
        .filter(models.Exercise.deleted==None)\
        .order_by(models.Exercise.name)\
        .all()

    return all_models


# @router.get(
#     '/{id}',
#     response_model=schemas.ExerciseOut
# )
# def get_by_id(
#     id: int,
#     db: Session = Depends(get_db),
#     current_user: schemas.UserOut = Depends(oauth2.get_current_user)
# ):
#     model = db.query(models.Exercise)\
#         .filter(
#             models.Exercise.xid == id
#         ).first()
   
#     if not model:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail='Model not found'
#         )


#     if model.xid!=current_user.xid:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not authorized to perform requested action"
#         )

#     return model





# soft delete
@router.delete(
    "/{id}",
    response_model=schemas.ExerciseOut,

    # status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    
    query = db.query(models.Exercise)\
        .filter(models.Exercise.xid == id)

    model: models.Exercise = query.first()

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model was not found"
        )

    if model.user_xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    # model_query.delete(synchronize_session=False)

    # db.commit()

    query.update(
        {
            "deleted": datetime.now(timezone.utc)
        },
        synchronize_session=False
    )

    db.commit()



    return query.first()
    # return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put(
    "/{id}",
    response_model=schemas.ExerciseOut,
)
def update(
    id: int,
    update_schema: schemas.ExerciseUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    query = db \
        .query(models.Exercise)\
        .filter(models.Exercise.xid == id)

    model = query.first()

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        ) 

    if model.user_xid!=current_user.xid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )

    query.update(
        update_schema.model_dump(exclude_none=True),
        synchronize_session=False
    )

    db.commit()

    return query.first()