from fastapi import APIRouter, Depends, status, HTTPException
from server import models, schemas, oauth2
from server.utils import verify
from server.database import get_db
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(
    tags=['Authentication'],   
)

@router.post(
    "/login",
    response_model=schemas.Token
)
def login(
    user_credentials: OAuth2PasswordRequestForm=Depends(),
    db: Session=Depends(get_db)
):
    user = db.query(models.User)\
        .filter(models.User.email==user_credentials.username)\
        .first()


    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(
        data = {
            "xid" : user.xid
        }
    )
    
    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }

