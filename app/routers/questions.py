from fastapi import APIRouter

router = APIRouter()


@router.get("/questions")
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
        },
        {
            "id": 6,
            "question": "Do you have high blood pressure?",
            "type": "boolean"
        },
        {
            "id": 7,
            "question": "Does your household have health insurance coverage?",
            "type": "boolean"
        },
        {
            "id": 8,
            "question": "How many hours do you sleep per night?",
            "type": "number"
        },
        {
            "id": 9,
            "question": "How many people live in your household?",
            "type": "number"
        },
        {
            "id": 10,
            "question": "Did anyone in your household need medical care but not receive it in the last 12 months?",
            "type": "boolean"
        }
    ]