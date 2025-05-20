from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None = None
    is_active: bool

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
