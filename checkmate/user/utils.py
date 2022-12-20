from typing import Optional

from sqlmodel import Session, select

from checkmate.database import engine
from checkmate.user.models import User


def get_user(username) -> Optional[User]:
    """Get user from database"""
    query = select(User).where(User.username == username)
    with Session(engine) as session:
        return session.exec(query).first()
