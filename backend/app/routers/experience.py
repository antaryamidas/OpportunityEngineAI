from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.experience import (
    ExperienceCreate,
    ExperienceResponse,
)
from app.services.experience_service import (
    create_experience,
    get_all_experiences,
    update_experience,
    delete_experience
)

router = APIRouter(
    prefix="/experience",
    tags=["Experience"]
)


@router.post(
    "",
    response_model=ExperienceResponse
)
def add_experience(
    experience: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_experience(
        db=db,
        current_user=current_user,
        experience=experience
    )

@router.get(
    "",
    response_model=list[ExperienceResponse]
)
def get_experiences(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_experiences(
        db=db,
        current_user=current_user
    )
@router.put(
    "/{experience_id}",
    response_model=ExperienceResponse
)
def edit_experience(
    experience_id: int,
    experience: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return update_experience(
            db=db,
            current_user=current_user,
            experience_id=experience_id,
            experience_data=experience
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    
@router.delete("/{experience_id}")
def remove_experience(
    experience_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return delete_experience(
            db=db,
            current_user=current_user,
            experience_id=experience_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )