from fastapi import FastAPI

from app.database import Base, engine
import app.models

from app.routers import questions
from app.routers import surveys
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Noon.HealthAI API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "status": "RENDER_TEST_123"
    }

app.include_router(questions.router)
app.include_router(surveys.router)
app.include_router(auth.router)