from fastapi import FastAPI
from app.routers import auth, users, resume

app = FastAPI(title="AI Resume Screener")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(resume.router)
