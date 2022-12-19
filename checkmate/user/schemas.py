from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    username: constr(
        regex="^[A-Za-z0-9-_]+$",
        to_lower=True,
        strip_whitespace=True,
        min_length=3,
        max_length=20,
    )
    email: EmailStr
    password: str
    avatar: Optional[str]
    active: bool = True

    class Config:
        orm_mode = True


class UserRequest(UserBase):
    ...


class UserResponse(UserBase):
    id: int
