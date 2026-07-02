from pydantic import BaseModel, HttpUrl
from typing import Optional


class ProfileCreate(BaseModel):
    headline: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[HttpUrl] = None
    github_url: Optional[HttpUrl] = None
    portfolio_url: Optional[HttpUrl] = None


class ProfileResponse(ProfileCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True