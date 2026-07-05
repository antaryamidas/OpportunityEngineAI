from sqlalchemy.orm import Session

from app.models.experience import Experience
from app.models.user import User
from app.schemas.experience import ExperienceCreate


def create_experience(
    db: Session,
    current_user: User,
    experience: ExperienceCreate
):
    new_experience = Experience(
        user_id=current_user.id,
        company=experience.company,
        job_title=experience.job_title,
        employment_type=experience.employment_type,
        location=experience.location,
        start_date=experience.start_date,
        end_date=experience.end_date,
        currently_working=experience.currently_working,
        description=experience.description,
    )

    db.add(new_experience)
    db.commit()
    db.refresh(new_experience)

    return new_experience

def get_all_experiences(
    db: Session,
    current_user: User
):
    return (
        db.query(Experience)
        .filter(Experience.user_id == current_user.id)
        .all()
    )

def update_experience(
    db: Session,
    current_user: User,
    experience_id: int,
    experience_data: ExperienceCreate
):
    experience = (
        db.query(Experience)
        .filter(
            Experience.id == experience_id,
            Experience.user_id == current_user.id
        )
        .first()
    )

    if not experience:
        raise ValueError("Experience not found")

    experience.company = experience_data.company
    experience.job_title = experience_data.job_title
    experience.employment_type = experience_data.employment_type
    experience.location = experience_data.location
    experience.start_date = experience_data.start_date
    experience.end_date = experience_data.end_date
    experience.currently_working = experience_data.currently_working
    experience.description = experience_data.description

    db.commit()
    db.refresh(experience)

    return experience

def delete_experience(
    db: Session,
    current_user: User,
    experience_id: int
):
    experience = (
        db.query(Experience)
        .filter(
            Experience.id == experience_id,
            Experience.user_id == current_user.id
        )
        .first()
    )

    if not experience:
        raise ValueError("Experience not found")

    db.delete(experience)
    db.commit()

    return {"message": "Experience deleted successfully"}