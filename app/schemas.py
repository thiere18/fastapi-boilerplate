from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
class PostCreate(PostBase):
    pass
    




class Post(PostBase):
    id: int
    
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True

        
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime    
    class Config:
        orm_mode = True




class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    owner: UserOut

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

