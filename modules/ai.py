import os
from google import genai

# -------------------------------
# Gemini Client
# -------------------------------

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# -------------------------------
# AI Resume Review
# -------------------------------

def ai_resume_review(resume_text, job_description):

    prompt = f"""
You are a Senior Google Machine Learning Recruiter.

Analyze this resume against the given Job Description.

Return the response in markdown.

Resume:

{resume_text}


Job Description:

{job_description}


Give:

# ATS Review

Overall Score (/100)

Matched Skills

Missing Skills

Strengths

Weaknesses

Resume Improvements

Interview Chances

Final Recruiter Verdict
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -------------------------------
# Career Roadmap
# -------------------------------

def generate_career_roadmap(resume_text):

    prompt = f"""
You are an AI Career Mentor.

Resume:

{resume_text}

Generate a roadmap for next 12 months.

Include:

Month 1

Month 2

Month 3

...

Month 12

Certifications

Projects

Interview Preparation

Final Advice
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -------------------------------
# Resume Optimizer
# -------------------------------

def optimize_resume(resume_text):

    prompt = f"""
Improve this resume professionally.

Resume:

{resume_text}

Improve

Professional Summary

Projects

Experience

Skills

Achievements

Return in markdown.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text