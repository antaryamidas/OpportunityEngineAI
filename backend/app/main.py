from fastapi import FastAPI

from app.routers.auth import router as auth_router

app = FastAPI(
    title="Opportunity Engine AI",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Opportunity Engine AI"
    }