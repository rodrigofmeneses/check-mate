from datetime import timedelta

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from checkmate.config import settings
from checkmate.user import User

from .models import Token
from .utils import authenticate_user, create_access_token, get_user

ACCESS_TOKEN_EXPIRE_MINUTES = settings.security.access_token_expire_minutes

router = APIRouter(tags=["auth"], prefix="/api/auth")


@router.post("/token", response_model=Token, status_code=status.HTTP_200_OK)
def login_for_access_token(*, form: OAuth2PasswordRequestForm = Depends()):
    """Create a user"""
    user = authenticate_user(get_user, form.username, form.password)

    if not user or not isinstance(user, User):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"username": user.username}, expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
