from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr

class User(UserBase):
    id: int
    is_active: bool = False
    
class UserCreate(User):
    pass
