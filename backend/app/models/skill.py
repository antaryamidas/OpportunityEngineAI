from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    skill_name = Column(String(100), nullable=False)

    skill_level = Column(String(50))

    years_of_experience = Column(Integer)

    user = relationship(
        "User",
        back_populates="skills"
    )