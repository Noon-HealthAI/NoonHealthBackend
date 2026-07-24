from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Dict, Any
import json

from database import SessionLocal, engine, Base
from models import SurveyResponseDB

Base.metadata.create_all(bind=engine)

app = FastAPI()


class SurveySubmission(BaseModel):
    organization: str
    responses: Dict[str, Any]


@app.get("/")
def root():
    return {
        "status": "Noon.HealthAI Running"
    }


@app.get("/questions")
def questions():
    return [
        {
            "id": 1,
            "question": "What is your age?",
            "type": "number"
        },
        {
            "id": 2,
            "question": "Do you smoke?",
            "type": "boolean"
        },
        {
            "id": 3,
            "question": "Do you have diabetes?",
            "type": "boolean"
        },
        {
            "id": 4,
            "question": "Do you exercise regularly?",
            "type": "boolean"
        },
        {
            "id": 5,
            "question": "Gender",
            "type": "text"
        }
    ]


@app.post("/responses")
def submit_response(submission: SurveySubmission):

    db: Session = SessionLocal()

    survey = SurveyResponseDB(
        organization=submission.organization,
        responses=json.dumps(submission.responses)
    )

    db.add(survey)
    db.commit()
    db.refresh(survey)

    response_id = survey.id

    db.close()

    return {
        "message": "Survey stored successfully",
        "id": response_id
    }


@app.get("/responses")
def get_all_responses():

    db: Session = SessionLocal()

    surveys = db.query(SurveyResponseDB).all()

    result = []

    for survey in surveys:
        result.append({
            "id": survey.id,
            "organization": survey.organization,
            "responses": json.loads(survey.responses)
        })

    db.close()

    return result