<div align="center">

# 🚀 SkillLens AI

### AI Career Intelligence Platform

<p align="center">
AI-powered platform that helps students analyze resumes, optimize ATS scores, match jobs, generate career roadmaps, prepare for interviews, and simulate recruiter feedback using Google's Gemini AI.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)

![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)

![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge)

![Gemini AI](https://img.shields.io/badge/Gemini-AI-blueviolet?style=for-the-badge)

![Scikit Learn](https://img.shields.io/badge/scikit--learn-ML-yellow?style=for-the-badge&logo=scikitlearn)

![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)

</p>

---

### 💡 Built to solve a real problem

Most resume analyzers only calculate an ATS score.

**SkillLens AI** goes much further.

It combines Resume Analysis, ATS Evaluation, Job Matching, Resume Optimization, Career Roadmaps, Interview Preparation, and Recruiter Simulation into one AI-powered platform.

Instead of giving users only a score, it explains **why** the score is low and **how** to improve it.

---

## ✨ Live Demo

(https://skilllens-ai-final-bw52mpb4ucjv97nc6jpp2c.streamlit.app/)

---



# 📖 Project Story

Every year millions of students apply for internships and placements.

Most resumes are rejected before a recruiter even reads them.

The biggest challenge isn't a lack of talent—it's the inability to understand what recruiters and ATS systems actually expect.

SkillLens AI was built to bridge this gap.

Instead of simply giving an ATS score, the platform explains:

- Why your resume is weak
- Which skills are missing
- Which projects need improvement
- Which technologies recruiters expect
- How likely you are to get shortlisted
- What you should learn over the next 12 months

The goal was to build something that feels like a real AI product instead of another college project.

# 🌟 Key Features

- 📄 Resume Analysis
- 🤖 AI Resume Review using Gemini
- 🎯 Hybrid ATS Score
- 📊 Skill Match Engine
- 🚀 Resume Optimizer
- 💼 Job Matching
- 🛣️ AI Career Roadmap Generator
- 🎤 Interview Preparation
- 👨‍💼 Recruiter Dashboard
- 📈 Interactive Charts
- 📥 Downloadable Reports

- # 🏗️ Project Architecture

```text
                     Resume PDF
                           │
                           ▼
                Resume Text Extraction
                           │
                           ▼
               Skill Extraction Engine
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   ATS Engine        Job Matching      Resume Optimizer
        │                  │                  │
        └──────────────┬───┴──────────────────┘
                       ▼
                 Gemini AI Review
                       ▼
             Career Intelligence Report
```
# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3.13 |
| Frontend | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Resume Parsing | PyPDF2 |
| Visualization | Plotly |
| Version Control | Git & GitHub |
| Deployment | Streamlit Cloud |

# 📂 Project Structure

```text
SkillLens-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
├── components/
├── data/
├── modules/
├── notebooks/
├── pages/
├── styles/
└── utils/
```
# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/krishmittal2305/SkillLens-AI-Final.git
```

Move into project

```bash
cd SkillLens-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```
# 🔐 Environment Variables

Create a `.streamlit/secrets.toml` file or configure the following environment variable:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

The API key is **not stored inside the source code** for security reasons.
