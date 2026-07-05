from sqlalchemy.orm import Session

from app.models.skill import Skill
from app.models.user import User
from app.schemas.skill import SkillCreate


def create_skill(
    db: Session,
    current_user: User,
    skill: SkillCreate
):
    new_skill = Skill(
        user_id=current_user.id,
        skill_name=skill.skill_name,
        skill_level=skill.skill_level,
        years_of_experience=skill.years_of_experience
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)

    return new_skill


def get_all_skills(
    db: Session,
    current_user: User
):
    return (
        db.query(Skill)
        .filter(Skill.user_id == current_user.id)
        .all()
    )


def update_skill(
    db: Session,
    current_user: User,
    skill_id: int,
    skill_data: SkillCreate
):
    skill = (
        db.query(Skill)
        .filter(
            Skill.id == skill_id,
            Skill.user_id == current_user.id
        )
        .first()
    )

    if not skill:
        raise ValueError("Skill not found")

    skill.skill_name = skill_data.skill_name
    skill.skill_level = skill_data.skill_level
    skill.years_of_experience = skill_data.years_of_experience

    db.commit()
    db.refresh(skill)

    return skill


def delete_skill(
    db: Session,
    current_user: User,
    skill_id: int
):
    skill = (
        db.query(Skill)
        .filter(
            Skill.id == skill_id,
            Skill.user_id == current_user.id
        )
        .first()
    )

    if not skill:
        raise ValueError("Skill not found")

    db.delete(skill)
    db.commit()

    return {
        "message": "Skill deleted successfully"
    }