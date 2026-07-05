from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.services.education_service import create_education
from app.schemas.education import (
    EducationCreate,
    EducationResponse
)

from app.services.education_service import (
    create_education,
    update_education,
    get_all_educations,
    delete_education
)

router = APIRouter(
    prefix="/education",
    tags=["Education"]
)


@router.post(
    "",
    response_model=EducationResponse
)
def add_education(
    education: EducationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_education(
        db=db,
        current_user=current_user,
        education=education
    )

@router.get(
    "",
    response_model=list[EducationResponse]
)
def get_educations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_educations(
        db=db,
        current_user=current_user
    )

@router.put(
    "/{education_id}",
    response_model=EducationResponse
)
def edit_education(
    education_id: int,
    education: EducationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return update_education(
            db=db,
            current_user=current_user,
            education_id=education_id,
            education_data=education
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.delete("/{education_id}")
def remove_education(
    education_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return delete_education(
            db=db,
            current_user=current_user,
            education_id=education_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )   

