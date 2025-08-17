from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze")
def analyze_data():
    return {"message": "Analyze endpoint works!"}
