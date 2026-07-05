from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.skill import SkillCreate, SkillResponse

from app.services.skill_service import (
    create_skill,
    get_all_skills,
    update_skill,
    delete_skill
)

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)


@router.post(
    "",
    response_model=SkillResponse
)
def add_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_skill(
        db=db,
        current_user=current_user,
        skill=skill
    )


@router.get(
    "",
    response_model=list[SkillResponse]
)
def get_skills(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_skills(
        db=db,
        current_user=current_user
    )


@router.put(
    "/{skill_id}",
    response_model=SkillResponse
)
def edit_skill(
    skill_id: int,
    skill: SkillCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return update_skill(
            db=db,
            current_user=current_user,
            skill_id=skill_id,
            skill_data=skill
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.delete("/{skill_id}")
def remove_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return delete_skill(
            db=db,
            current_user=current_user,
            skill_id=skill_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )