from enum import Enum


class TaskStatus(str, Enum):
    """Takes a plain text and valid if enum type
    class Task(SQLModel, table=True):
        status: TaskStatus
    """

    TODO = "TODO"
    DOING = "DOING"
    DONE = "DONE"

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        """Accepts a plain text"""
        if not isinstance(value, str):
            raise TypeError("string required")

        if value not in (TaskStatus.TODO, TaskStatus.DOING, TaskStatus.DONE):
            raise ValueError("must be value TODO, DOING or DONE")

        return cls(value)

    def __repr__(self):
        return self.value
