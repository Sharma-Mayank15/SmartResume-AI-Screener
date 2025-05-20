from fastapi import APIRouter, UploadFile, File, Form

router = APIRouter(prefix="/resume", tags=["resume"])

@router.post("/analyze")
async def analyze_resume(job_description: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()
    score = 85
    feedback = f"Resume scored {score} based on job description."
    return {"score": score, "feedback": feedback}
