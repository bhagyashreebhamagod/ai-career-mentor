from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from database import resumes_collection
from agent import analyze_resume
from graph.workflow import workflow
import os

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
    return {"message": "Resume stored successfully"}


@app.post("/analyze")
def analyze(resume: Resume):

    analysis = analyze_resume(resume.skills)

    resumes_collection.insert_one({
        "name": resume.name,
        "email": resume.email,
        "skills": resume.skills,
        "analysis": analysis
    })

    return {
        "name": resume.name,
        "analysis": analysis
    }


@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = workflow.invoke({
        "file_path": file_path
    })

    resumes_collection.insert_one({
        "file_name": file.filename,
        "resume_text": result["resume_text"],
        "skills": result["skills"],
        "career_recommendations": result["careers"],
        "learning_roadmap": result["roadmap"],
        "interview_questions": result["interview_questions"]
    })

    return {
        "message": "Resume analyzed successfully",
        "result": result
    }
