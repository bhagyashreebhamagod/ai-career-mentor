from agent import client

def extract_skills(resume_text):

    prompt = f"""
Extract only the technical skills from this resume.

Return them as a Python list.

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
