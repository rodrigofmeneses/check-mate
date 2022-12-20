from typing import List, Optional

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

from checkmate.security import HashedPassword


class User(SQLModel, table=True):
    """Represents the User Model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False)
    email: EmailStr = Field(unique=True)
    password: HashedPassword
    avatar: Optional[str]
    active: bool = True

    tasks: List["Task"] = Relationship(back_populates="user")
