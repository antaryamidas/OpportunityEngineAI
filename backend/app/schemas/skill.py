from pydantic import BaseModel
from typing import Optional


class SkillCreate(BaseModel):
    skill_name: str
    skill_level: Optional[str] = None
    years_of_experience: Optional[int] = None


class SkillResponse(SkillCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True