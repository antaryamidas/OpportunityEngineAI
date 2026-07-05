from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Text
from sqlalchemy.orm import relationship

from app.database.base import Base


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    company = Column(String(200), nullable=False)

    job_title = Column(String(150), nullable=False)

    employment_type = Column(String(50))

    location = Column(String(100))

    start_date = Column(Date)

    end_date = Column(Date)

    currently_working = Column(Boolean, default=False)

    description = Column(Text)

    user = relationship(
        "User",
        back_populates="experiences"
    )