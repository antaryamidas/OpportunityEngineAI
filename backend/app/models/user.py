from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(120), unique=True, index=True, nullable=False)

    phone = Column(String(20), unique=True, nullable=True)

    password_hash = Column(String(255), nullable=False)

    role = Column(String(20), default="user")

    is_verified = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    profile = relationship(
        "UserProfile",
        back_populates="user",
        uselist=False
)