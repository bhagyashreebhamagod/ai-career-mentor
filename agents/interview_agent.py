from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def interview(skills):
    prompt = f"""
Generate 20 interview questions for these skills:

{skills}

Include:
- Beginner
- Intermediate
- Advanced
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
