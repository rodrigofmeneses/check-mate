from typing import List, Optional

from fastapi import Depends

from checkmate.auth.utils import AuthenticatedUser
from checkmate.database import ActiveSession, Session
from checkmate.tasks.models import Task
from checkmate.user.models import User

# session: Session = ActiveSession


class Services:
    """CRUD Business Logic"""

    def __init__(self, session: Session = ActiveSession):
        self.session = session

    def create(self, task: Task) -> Task:
        self.session.add(task)
        self.session.commit()
        return task

    def find_all(self) -> List[Task]:
        ...

    def find_by_id(self, task_id: int) -> Optional[Task]:
        ...

    def update(self, task_id: int) -> Optional[Task]:
        ...

    def delete(self, task_id: int) -> Optional[Task]:
        ...


TaskService = Depends(Services)
