from fastapi import APIRouter

router = APIRouter()

@router.get("/questions")
def questions():
    return {
        "debug": "THIS IS THE NEW FILE"
    }