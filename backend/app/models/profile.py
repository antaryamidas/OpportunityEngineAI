from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.database.base import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    headline = Column(String(200))

    bio = Column(Text)

    location = Column(String(100))

    linkedin_url = Column(String(255))

    github_url = Column(String(255))

    portfolio_url = Column(String(255))

    user = relationship(
        "User",
        back_populates="profile"
    )