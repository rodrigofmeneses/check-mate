from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """Represents the User Model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False)
    email: EmailStr = Field(unique=True)
    password: str
    avatar: Optional[str] = None
    active: bool = True
