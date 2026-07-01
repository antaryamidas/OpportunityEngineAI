from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    phone: Optional[str] = None
    password: str = Field(..., min_length=8, max_length=100)


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: Optional[str]
    role: str
    is_verified: bool

    class Config:
        from_attributes = True