from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated
from datetime import datetime

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
class PostBase(BaseModel):

    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):

    pass

class PostUpdate(PostBase):

    title: str
    content: str
    published: bool = True

class UserCreate(BaseModel):

    email: EmailStr
    password : str

class UserOut(BaseModel):

    id: int
    email: EmailStr
    created_at: datetime

class Post(PostBase):

    id: int
    created_at: datetime
    owner_id:int
    owner: UserOut

class PostOut(BaseModel):

    Post: Post
    votes: int

class UserLogin(BaseModel):

    email: EmailStr
    password: str

class Token(BaseModel):
    access_token :str
    token_type: str

class TokenData(BaseModel):
    id: int

class Vote(BaseModel):
    
    post_id: int
    dir: Annotated[int, Field(strict=True, ge=-1, le=1)]



    
    

    