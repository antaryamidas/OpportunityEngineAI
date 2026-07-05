from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    degree = Column(String(150), nullable=False)

    institution = Column(String(200), nullable=False)

    field_of_study = Column(String(150))

    start_year = Column(Integer)

    end_year = Column(Integer)

    grade = Column(String(50))

    description = Column(String(500))

    user = relationship(
        "User",
        back_populates="educations"
    )