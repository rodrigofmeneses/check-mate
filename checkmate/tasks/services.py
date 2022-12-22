from typing import List, Optional

from fastapi import Depends, HTTPException, status
from sqlmodel import select

from checkmate.auth.utils import AuthenticatedUser
from checkmate.database import ActiveSession, Session
from checkmate.user.models import User

from .models import Task
from .schemas import TaskRequest


class Services:
    """CRUD Business Logic"""

    def __init__(
        self, session: Session = ActiveSession, user: User = AuthenticatedUser
    ):
        self.session = session
        self.user = user

    def create(self, task_body: TaskRequest) -> Task:
        task_body.user_id = self.user.id
        task = Task.from_orm(task_body)
        self.session.add(task)
        self.session.commit()
        return task

    def find_all(self) -> List[Task]:
        return self.session.exec(
            select(Task).where(Task.user_id == self.user.id)
        ).all()

    def find_by_id(self, task_id: int) -> Optional[Task]:
        task = self.check_valid_task_by_id(task_id)
        return task

    def update(self, task_id: int, task_body: TaskRequest) -> Optional[Task]:
        task = self.check_valid_task_by_id(task_id)
        task_data = task_body.dict(exclude_unset=True)

        for key, value in task_data.items():
            setattr(task, key, value)

        self.session.add(task)
        self.session.commit()
        return task

    def delete(self, task_id: int) -> Optional[Task]:
        task = self.check_valid_task_by_id(task_id)
        self.session.delete(task)
        self.session.commit()
        return {"msg": f"Task {task.id} Deleted", "task": task}

    def get_task(self, task_id: int) -> Task:
        """Get a task by id"""
        task = self.session.get(Task, task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )
        return task

    def check_valid_task_by_id(self, task_id: int) -> Task:
        """Checks if the task belongs to the user"""
        task = self.get_task(task_id)
        if task.user.id != self.user.id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No Permission to access another user task",
            )
        return task


TaskService = Depends(Services)
