from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from .utils import TaskStatus


class Task(SQLModel, table=True):
    """Represents the Task Model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    status: TaskStatus = Field(default=TaskStatus.TODO)
    creation_date: datetime = Field(default_factory=datetime.now)
    update_date: datetime = Field(default_factory=datetime.now)

    user_id: int = Field(foreign_key="user.id")

    user: "User" = Relationship(back_populates="tasks")