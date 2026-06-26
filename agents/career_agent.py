from agent import client

def recommend_career(skills):

    prompt = f"""
Based on these skills:

{skills}

Suggest:

1. Best Job Roles

2. Salary Range

3. Companies Hiring
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
