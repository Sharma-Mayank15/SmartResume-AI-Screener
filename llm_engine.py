import openai
import os

openai.api_key ={"Open API Key"}
def analyze_resume(resume_text: str, job_desc: str) -> dict:
    prompt = f"""
You are an AI assistant. Analyze the following resume and job description.
Give a score out of 100 and suggest strengths and areas to improve.

Resume:
{resume_text}

Job Description:
{job_desc}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return {"analysis": response["choices"][0]["message"]["content"]}
