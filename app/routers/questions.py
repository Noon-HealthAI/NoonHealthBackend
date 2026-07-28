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
        }
    ]