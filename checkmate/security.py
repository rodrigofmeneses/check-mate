"""Security utilities"""
from passlib.context import CryptContext

from checkmate.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = settings.security.secret_key
ALGORITHM = settings.security.algorithm


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a hash against a password"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Generates a hash from plain text"""
    return pwd_context.hash(password)


class HashedPassword(str):
    """Takes a plain text password and hashes it.
    use this as a field in your SQLModel
    class User(SQLModel, table=True):
        password: HashedPassword
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """Accepts a plain text password and returns a hashed password."""
        if not isinstance(v, str):
            raise TypeError("string required")

        hashed_password = get_password_hash(v)
        return cls(hashed_password)
