from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
def get_my_profile(
    current_user: User = Depends(get_current_user)
):
    return current_user