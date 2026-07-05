from pydantic import BaseModel
from typing import Optional


class EducationCreate(BaseModel):
    degree: str
    institution: str
    field_of_study: Optional[str] = None
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    grade: Optional[str] = None
    description: Optional[str] = None


class EducationResponse(EducationCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True