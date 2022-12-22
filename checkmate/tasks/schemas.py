from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra

from checkmate.tasks.utils import TaskStatus


class TaskBase(BaseModel):
    """Serializer Task Base"""

    title: str
    description: str

    class Config:
        orm_mode = True


class TaskRequest(TaskBase):
    """Serializer for Task request payload"""

    status: Optional[TaskStatus]

    class Config:
        extra = Extra.allow
        arbitrary_types_allowed = True


class TaskResponse(TaskBase):
    """Serializer for Task response"""

    id: int
    status: TaskStatus
    creation_date: datetime
    update_date: datetime
    user_id: int


class UpdateTaskRequest(TaskRequest):
    """Serializer for update Task response"""

    title: Optional[str]
    description: Optional[str]
    status: Optional[TaskStatus]
