from fastapi import FastAPI

from checkmate import main_router

app = FastAPI(
    title="CheckMate",
    version="0.1.0",
    description="Todo list APP to CheckMate your tasks",
)

app.include_router(main_router)
