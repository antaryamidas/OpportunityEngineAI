from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.profile import router as profile_router

app = FastAPI(
    title="Opportunity Engine AI",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(profile_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Opportunity Engine AI"
    }