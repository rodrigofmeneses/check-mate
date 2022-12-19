from fastapi import APIRouter

from checkmate import user

main_router = APIRouter()

main_router.include_router(user.router)
