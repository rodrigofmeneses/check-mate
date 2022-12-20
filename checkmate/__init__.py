from fastapi import APIRouter
from sqlmodel import SQLModel

from checkmate import auth, user
from checkmate.tasks import Task
from checkmate.user import User

main_router = APIRouter()

main_router.include_router(user.router)
main_router.include_router(auth.router)

__all__ = ["SQLModel", "Task", "User"]
