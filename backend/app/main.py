from fastapi import FastAPI

app = FastAPI(
    title="Opportunity Engine AI",
    description="AI-Powered Job Discovery and Resume Optimization Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Opportunity Engine AI 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "Running",
        "database": "PostgreSQL",
        "backend": "FastAPI"
    }