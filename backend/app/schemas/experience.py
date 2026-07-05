from datetime import date
from typing import Optional

from pydantic import BaseModel


class ExperienceCreate(BaseModel):
    company: str
    job_title: str
    employment_type: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    currently_working: bool = False
    description: Optional[str] = None


class ExperienceResponse(ExperienceCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True