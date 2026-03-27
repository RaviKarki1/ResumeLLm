from fastapi import APIRouter
from app.models.request_models import AnalyzeRequest

router = APIRouter()

@router.post("/analyze")
def analyze_resume(data: AnalyzeRequest):
    return{
        "message":"Analyze endpoint working",
        "resume_length":len(data.resume_text),
        "jd_length":len(data.job_description)
    }
