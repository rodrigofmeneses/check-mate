from fastapi import APIRouter, status

from checkmate.auth.utils import AuthenticatedUser
from checkmate.user.models import User

from .models import Task
from .schemas import TaskRequest, TaskResponse
from .services import Services, TaskService

router = APIRouter(tags=["tasks"], prefix="/api/tasks")


@router.post(
    "/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED
)
def create_task(
    *,
    task: TaskRequest,
    task_service: Services = TaskService,
    user: User = AuthenticatedUser
):
    """Create a task"""
    task.user_id = user.id
    db_task = Task.from_orm(task)
    return task_service.create(db_task)
