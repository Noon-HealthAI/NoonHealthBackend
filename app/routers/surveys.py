from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json

from app.database import SessionLocal
from app.models import SurveyResponseDB
from app.schemas import SurveySubmission
from app.security import get_current_user


router = APIRouter(
    tags=["Surveys"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/responses")
def submit_response(
    submission: SurveySubmission,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    survey = SurveyResponseDB(
        organization=current_user["organization"],
        responses=json.dumps(submission.responses)
    )

    db.add(survey)
    db.commit()
    db.refresh(survey)

    return {
        "message": "Survey stored successfully",
        "id": survey.id,
        "organization": current_user["organization"]
    }


@router.get("/responses")
def get_all_responses(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    surveys = (
        db.query(SurveyResponseDB)
        .filter(
            SurveyResponseDB.organization ==
            current_user["organization"]
        )
        .all()
    )

    result = []

    for survey in surveys:
        result.append({
            "id": survey.id,
            "organization": survey.organization,
            "responses": json.loads(survey.responses)
        })

    return result