from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.profile import router as profile_router
from app.routers.education import router as education_router
from app.routers.experience import router as experience_router
from app.routers.skills import router as skills_router

app = FastAPI(
    title="Opportunity Engine AI",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(profile_router)
app.include_router(education_router)
app.include_router(experience_router)
app.include_router(skills_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Opportunity Engine AI"
    }