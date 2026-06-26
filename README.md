# 🚀 AI Career Mentor

An AI-powered career guidance application built with **FastAPI**, **MongoDB Atlas**, and **Google Gemini AI**. This project helps users store resume information, analyze their technical skills, identify skill gaps, receive career recommendations, and generate personalized learning roadmaps.

---

## 📌 Project Overview

AI Career Mentor is designed to help students and professionals understand their current skill set and receive AI-driven career guidance.

The application stores resume information in MongoDB Atlas and uses Google Gemini AI to generate intelligent recommendations such as:

* Suitable career roles
* Missing technical skills
* Personalized learning roadmap
* Interview preparation tips

This project demonstrates how modern AI can be integrated with backend technologies to build intelligent applications.

---

## Application Preview

### Swagger UI

<img width="1876" height="855" alt="image" src="https://github.com/user-attachments/assets/f5a2e14b-1172-4709-9a2c-018d2c1a3e5c" />


### AI Career Analysis

<img width="1814" height="911" alt="image" src="https://github.com/user-attachments/assets/780be87c-24f5-4d3d-a9dc-7b7e36686eb9" />

# ✨ Features

* Store resumes in MongoDB Atlas
* AI-powered career analysis
* Career recommendations
* Skill gap identification
* Personalized learning roadmap
* Interview preparation guidance
* REST APIs using FastAPI
* Input validation using Pydantic

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
        FastAPI REST API
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
 MongoDB Atlas         Gemini AI
(Store Resume)     (Career Analysis)
        │                   │
        └─────────┬─────────┘
                  ▼
           JSON Response
```

---

# 🛠 Tech Stack

| Technology       | Purpose               |
| ---------------- | --------------------- |
| Python           | Programming Language  |
| FastAPI          | REST API Framework    |
| MongoDB Atlas    | Cloud NoSQL Database  |
| PyMongo          | MongoDB Driver        |
| Google Gemini AI | AI Career Analysis    |
| Pydantic         | Request Validation    |
| Uvicorn          | ASGI Server           |
| dotenv           | Environment Variables |

---

# 📂 Project Structure

```
ai-career-mentor/

│
├── agent.py
├── database.py
├── main.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-career-mentor.git

cd ai-career-mentor
```

---

## Create Virtual Environment

Linux / macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create a `.env` file.

```
MONGO_URI=your_mongodb_connection_string

GEMINI_API_KEY=your_gemini_api_key
```

---

# Run Application

```bash
uvicorn main:app --reload
```

Application runs at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# REST API Endpoints

## Home

```
GET /
```

Response

```json
{
    "message":"AI Career Mentor API"
}
```

---

## Store Resume

```
POST /resume
```

Example Request

```json
{
  "name":"Bhagyashree",
  "email":"bhagya@example.com",
  "skills":[
      "Python",
      "SQL",
      "MongoDB"
  ]
}
```

Response

```json
{
    "message":"Resume stored successfully"
}
```

---

## Analyze Resume

```
POST /analyze
```

Example Request

```json
{
  "name":"Bhagyashree",
  "email":"bhagya@example.com",
  "skills":[
      "Python",
      "SQL",
      "MongoDB"
  ]
}
```

Example Response

```json
{
  "name":"Bhagyashree",
  "analysis":"Recommended Career Roles...\nMissing Skills...\nLearning Roadmap...\nInterview Tips..."
}
```

---

# MongoDB Collections

```
career_db

└── resumes
```

Future collections

```
analysis

users

roadmaps

chat_history
```

---

# Example Workflow

```
User submits resume

        │

        ▼

FastAPI receives request

        │

        ▼

Resume stored in MongoDB

        │

        ▼

Gemini AI analyzes skills

        │

        ▼

Career recommendations generated

        │

        ▼

JSON response returned
```

---

# Future Enhancements

* Resume PDF Upload
* Resume Parsing
* Skill Extraction
* LangGraph Multi-Agent Workflow
* Interview Question Generator
* Docker Support
* JWT Authentication
* CI/CD with GitHub Actions
* Cloud Deployment
* AI Chat Assistant
* Vector Search with MongoDB Atlas

---

# Learning Outcomes

This project demonstrates practical experience with:

* FastAPI Development
* REST API Design
* MongoDB Atlas Integration
* AI Integration using Gemini
* Environment Variable Management
* Python Backend Development
* Git & GitHub
* API Testing using Swagger UI

---

# Author

**Bhagyashree Bamagod**

GitHub:
https://github.com/bhagyashreebhamagod

---

# License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

# 🚀 AI Career Mentor

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-success)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
