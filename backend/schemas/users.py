from typing import Optional, List
from pydantic import BaseModel
import uuid
from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    telegram: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    telegram: str
    username: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int
    carts: List['Cart'] = []

    class Config:
        orm_mode = True