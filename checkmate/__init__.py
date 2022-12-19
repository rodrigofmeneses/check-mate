from fastapi import APIRouter

from checkmate import auth, user

main_router = APIRouter()

main_router.include_router(user.router)
main_router.include_router(auth.router)
