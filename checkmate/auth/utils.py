"""Token absed auth"""
from datetime import datetime, timedelta
from typing import Callable, Optional, Union

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from checkmate.config import settings
from checkmate.security import verify_password
from checkmate.user import User
from checkmate.user.utils import get_user

from .schemas import TokenData

SECRET_KEY = settings.security.secret_key
ALGORITHM = settings.security.algorithm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


def create_access_token(data: dict, expires_delta: Optional[timedelta]) -> str:
    """Creates a JWT Token from user data"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "scope": "access_token"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(
    get_user: Callable, username: str, password: str
) -> Union[User, bool]:
    """Authenticate the user"""
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def get_current_user(
    token: str = Depends(oauth2_scheme), request: Request = None
) -> User:
    """Get current user authenticated"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if request:
        if authorization := request.headers.get("authorization"):
            try:
                token = authorization.split(" ")[1]
            except IndexError:
                raise credentials_exception

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")

        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """Wraps the sync get_active_user for sync calls"""
    return current_user


AuthenticatedUser = Depends(get_current_active_user)


async def validate_token(token: str = Depends(oauth2_scheme)) -> User:
    """Validates user token"""
    user = get_current_user(token=token)
    return user
