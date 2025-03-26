
from fastapi import APIRouter, status, HTTPException, Depends, Response
from server import schemas, models, oauth2
from server.database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone


router = APIRouter(
    prefix="/const_page_data",
    tags=['Const Page Data'],
)


@router.get(
    '/get_user_dashboard_const_data',
    response_model=schemas.UserDashboardConstData
)
def get_user_dashboard_const_data(
    # db: Session = Depends(get_db),
    # current_user: schemas.UserOut = Depends(oauth2.get_current_user)

):

    const_data_schema = schemas.UserDashboardConstData(
        targetMuscleOptions=["Option1"],
        targetMuscles=["Option1", "Option2", "Option3"]
    )

    return const_data_schema