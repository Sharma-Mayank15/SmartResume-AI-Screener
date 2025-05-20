from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from openai import OpenAI
import PyPDF2
import os
import io

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# FastAPI App setup
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount templates and static
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze/", response_class=HTMLResponse)
async def analyze_resume(
    request: Request,
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Read PDF content
    contents = await file.read()
    reader = PyPDF2.PdfReader(io.BytesIO(contents))
    resume_text = "".join([page.extract_text() for page in reader.pages if page.extract_text()])

    prompt = f"""
    You are an AI resume screener.
    Given the following job description and resume, evaluate the candidate’s suitability.
    
    Job Description:
    {job_description}
    
    Resume:
    {resume_text}
    
    Provide feedback with strengths, concerns, and a score out of 100.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert HR analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )

        analysis = response.choices[0].message.content.strip()
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": analysis
        })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": f"❌ Error: {str(e)}"
        })
