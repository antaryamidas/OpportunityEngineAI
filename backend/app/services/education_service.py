from sqlalchemy.orm import Session

from app.models.education import Education
from app.models.user import User
from app.schemas.education import EducationCreate


def create_education(
    db: Session,
    current_user: User,
    education: EducationCreate
):
    new_education = Education(
        user_id=current_user.id,
        degree=education.degree,
        institution=education.institution,
        field_of_study=education.field_of_study,
        start_year=education.start_year,
        end_year=education.end_year,
        grade=education.grade,
        description=education.description,
    )

    db.add(new_education)
    db.commit()
    db.refresh(new_education)

    return new_education

def get_all_educations(
    db: Session,
    current_user: User
):
    return (
        db.query(Education)
        .filter(Education.user_id == current_user.id)
        .all()
    )

def update_education(
    db: Session,
    current_user: User,
    education_id: int,
    education_data: EducationCreate
):
    education = (
        db.query(Education)
        .filter(
            Education.id == education_id,
            Education.user_id == current_user.id
        )
        .first()
    )

    if not education:
        raise ValueError("Education record not found")

    education.degree = education_data.degree
    education.institution = education_data.institution
    education.field_of_study = education_data.field_of_study
    education.start_year = education_data.start_year
    education.end_year = education_data.end_year
    education.grade = education_data.grade
    education.description = education_data.description

    db.commit()
    db.refresh(education)

    return education

def get_user_education(
    db: Session,
    user_id: int
):
    return (
        db.query(Education)
        .filter(Education.user_id == user_id)
        .all()
    )

def delete_education(
    db: Session,
    current_user: User,
    education_id: int
):
    education = (
        db.query(Education)
        .filter(
            Education.id == education_id,
            Education.user_id == current_user.id
        )
        .first()
    )

    if not education:
        raise ValueError("Education record not found")

    db.delete(education)
    db.commit()

    return {"message": "Education deleted successfully"}