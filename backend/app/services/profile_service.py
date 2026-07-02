from sqlalchemy.orm import Session

from app.models.profile import UserProfile
from app.models.user import User
from app.schemas.profile import ProfileCreate


def create_or_update_profile(
    db: Session,
    current_user: User,
    profile: ProfileCreate
):
    existing = (
        db.query(UserProfile)
        .filter(UserProfile.user_id == current_user.id)
        .first()
    )

    if existing:
        existing.headline = profile.headline
        existing.bio = profile.bio
        existing.location = profile.location
        existing.linkedin_url = str(profile.linkedin_url) if profile.linkedin_url else None
        existing.github_url = str(profile.github_url) if profile.github_url else None
        existing.portfolio_url = str(profile.portfolio_url) if profile.portfolio_url else None

        db.commit()
        db.refresh(existing)
        return existing

    new_profile = UserProfile(
        user_id=current_user.id,
        headline=profile.headline,
        bio=profile.bio,
        location=profile.location,
        linkedin_url=str(profile.linkedin_url) if profile.linkedin_url else None,
        github_url=str(profile.github_url) if profile.github_url else None,
        portfolio_url=str(profile.portfolio_url) if profile.portfolio_url else None,
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile