import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume(skills):
    prompt = f"""
    You are an AI Career Mentor.

    Candidate Skills:
    {', '.join(skills)}

    Please provide:

    1. Suitable job roles
    2. Missing technical skills
    3. 30-day learning roadmap
    4. Interview preparation tips
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
