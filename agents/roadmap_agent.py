from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def roadmap(skills):
    prompt = f"""
You are an AI Career Mentor.

Based on these skills:

{skills}

Create a detailed 30-day learning roadmap.

Include:
1. Topics to learn
2. Daily practice
3. Recommended projects
4. Resources
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
