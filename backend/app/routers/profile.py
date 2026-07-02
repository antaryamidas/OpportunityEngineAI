from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.profile import ProfileCreate, ProfileResponse
from app.services.profile_service import create_or_update_profile

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.post(
    "",
    response_model=ProfileResponse
)
def save_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_or_update_profile(
        db=db,
        current_user=current_user,
        profile=profile
    )