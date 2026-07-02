from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models AFTER Base is created
from app.models.user import User
from app.models.profile import UserProfile