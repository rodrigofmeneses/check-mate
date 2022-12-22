from typing import List

from fastapi import APIRouter, status

from .schemas import TaskRequest, TaskResponse, UpdateTaskRequest
from .services import Services, TaskService

router = APIRouter(tags=["tasks"], prefix="/api/tasks")


@router.post(
    "/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED
)
def create_task(*, task_body: TaskRequest, service: Services = TaskService):
    """Create a task"""
    return service.create(task_body)


@router.get(
    "/", response_model=List[TaskResponse], status_code=status.HTTP_200_OK
)
def user_tasks(*, service: Services = TaskService):
    """List all user tasks"""
    return service.find_all()


@router.get(
    "/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK
)
def user_task(*, task_id: int, service: Services = TaskService):
    """Get user task by id"""
    return service.find_by_id(task_id)


@router.patch(
    "/{task_id}",
    response_model=UpdateTaskRequest,
    status_code=status.HTTP_200_OK,
)
def update_task(
    *, task_body: TaskRequest, task_id: int, service: Services = TaskService
):
    """Update task by id"""
    return service.update(task_id, task_body)


@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(*, task_id: int, service: Services = TaskService):
    """Delete task by id"""
    return service.delete(task_id)
