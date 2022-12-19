from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from sqlmodel import Session

from checkmate.database import ActiveSession

from .models import User
from .schemas import UserRequest, UserResponse

router = APIRouter(tags=["user"], prefix="/api/users")


@router.post(
    "/", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(*, user: UserRequest, session: Session = ActiveSession):
    """Create a user"""
    db_user = User.from_orm(user)
    try:
        session.add(db_user)
        session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    return db_user
