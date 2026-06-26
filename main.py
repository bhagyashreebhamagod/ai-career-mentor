from fastapi import FastAPI
from pydantic import BaseModel
from database import resumes_collection
from agent import analyze_resume

app = FastAPI()


class Resume(BaseModel):
    name: str
    email: str
    skills: list


@app.get("/")
def home():
    return {"message": "AI Career Mentor API"}


@app.post("/resume")
def add_resume(resume: Resume):

    data = resume.dict()

    resumes_collection.insert_one(data)

    return {
        "message": "Resume stored successfully"
    }


@app.post("/analyze")
def analyze(resume: Resume):

    analysis = analyze_resume(resume.skills)

    return {
        "name": resume.name,
        "analysis": analysis
    }
