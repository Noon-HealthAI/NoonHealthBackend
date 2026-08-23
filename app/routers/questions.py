from fastapi import APIRouter

router = APIRouter()


@router.get("/questions")
def questions():
    return [
        {
            "id": 999,
            "question": "RENDER TEST QUESTION",
            "type": "text"
        }
    ]