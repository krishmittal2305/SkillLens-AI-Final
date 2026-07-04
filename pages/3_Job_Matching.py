import streamlit as st
import tempfile
import os
import sys

sys.path.append(os.getcwd())

from modules.parser import extract_resume_text, clean_text
from modules.skills import skills_database, smart_extract_skills, flatten_skill_map
from modules.ats import hybrid_ats_engine
from modules.charts import ats_gauge, skill_pie, radar_chart
from modules.ai import ai_resume_review

st.set_page_config(page_title="Job Matching", page_icon="🎯", layout="wide")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

.stApp {
    background:
    radial-gradient(circle at top left,rgba(59,130,246,.25),transparent 35%),
    radial-gradient(circle at top right,rgba(139,92,246,.28),transparent 35%),
    linear-gradient(135deg,#020617,#0f172a);
    color:white;
}

.block-container {
    max-width:1400px;
    padding-top:2rem;
}

.hero,.card,.upload-box {
    background:rgba(15,23,42,.80);
    border:1px solid rgba(255,255,255,.13);
    border-radius:28px;
    padding:30px;
    box-shadow:0 25px 70px rgba(0,0,0,.35);
}

.title {
    font-size:58px;
    font-weight:950;
    background:linear-gradient(90deg,#38bdf8,#8b5cf6,#22c55e);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle {
    color:#cbd5e1;
    font-size:18px;
    line-height:1.7;
}

.metric-card {
    padding:24px;
    border-radius:24px;
    background:rgba(15,23,42,.88);
    border:1px solid rgba(56,189,248,.25);
    text-align:center;
}

.metric-card h2 {
    font-size:44px;
    color:#38bdf8;
    margin:0;
}

.metric-card p {
    color:#cbd5e1;
}

.skill-chip {
    display:inline-block;
    padding:9px 15px;
    margin:6px;
    border-radius:999px;
    background:rgba(56,189,248,.14);
    border:1px solid rgba(56,189,248,.35);
    color:#bae6fd;
    font-weight:700;
}

.missing-chip {
    display:inline-block;
    padding:9px 15px;
    margin:6px;
    border-radius:999px;
    background:rgba(239,68,68,.14);
    border:1px solid rgba(239,68,68,.35);
    color:#fecaca;
    font-weight:700;
}

.big-btn button {
    background:linear-gradient(90deg,#2563eb,#7c3aed) !important;
    color:white !important;
    border-radius:18px !important;
    height:58px !important;
    font-weight:900 !important;
    border:0 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="title">AI Job Matching Dashboard</div>
    <div class="subtitle">
        Upload your resume and paste any job description. SkillLens AI compares your profile
        with the role, calculates match percentage, finds missing skills, and gives recruiter-style suggestions.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

left, right = st.columns([1, 1])

with left:
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    st.subheader("📄 Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    st.subheader("💼 Paste Job Description")
    job_description = st.text_area(
        "Job Description",
        height=260,
        value="""Machine Learning Engineer

Requirements:
Python, Machine Learning, SQL, Pandas, NumPy, Scikit-learn, Git, GitHub,
REST API, Docker, AWS, Streamlit, Data Structures, Algorithms.

Responsibilities:
Build ML models, deploy APIs, analyze datasets, collaborate with teams,
optimize ML pipelines, and create production-ready AI solutions."""
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

st.markdown('<div class="big-btn">', unsafe_allow_html=True)
match_btn = st.button("🎯 Match Resume With Job", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

if match_btn:

    if uploaded_file is None:
        st.error("Please upload a resume PDF first.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste a job description.")
        st.stop()

    with st.spinner("SkillLens AI is matching your resume with the job role..."):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        resume_text = extract_resume_text(temp_path)

        resume_skill_map = smart_extract_skills(resume_text, skills_database)
        resume_skills = flatten_skill_map(resume_skill_map)

        job_skill_map = smart_extract_skills(job_description, skills_database)
        job_skills = flatten_skill_map(job_skill_map)

        result = hybrid_ats_engine(
            resume_text,
            job_description,
            resume_skills,
            job_skills,
            clean_text
        )

    st.success("Job matching completed successfully.")

    st.write("")

    score = result["Final_ATS_Score"]

    if score >= 85:
        verdict = "Excellent Match"
    elif score >= 70:
        verdict = "Strong Match"
    elif score >= 55:
        verdict = "Moderate Match"
    else:
        verdict = "Low Match"

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{score}%</h2>
            <p>Job Match Score</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{result['Skill_Match_Score']}%</h2>
            <p>Skill Match</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{len(result['Matched_Skills'])}</h2>
            <p>Matched Skills</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="metric-card">
            <h2>{verdict}</h2>
            <p>Recruiter Verdict</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    ch1, ch2 = st.columns(2)

    with ch1:
        st.plotly_chart(
            ats_gauge(score),
            use_container_width=True
        )

    with ch2:
        st.plotly_chart(
            skill_pie(result["Matched_Skills"], result["Missing_Skills"]),
            use_container_width=True
        )

    st.write("")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✅ Skills Matching This Job")

    if result["Matched_Skills"]:
        st.markdown(
            "".join([f'<span class="skill-chip">{s}</span>' for s in result["Matched_Skills"]]),
            unsafe_allow_html=True
        )
    else:
        st.warning("No matched skills found.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚠️ Skills Missing For This Job")

    if result["Missing_Skills"]:
        st.markdown(
            "".join([f'<span class="missing-chip">{s}</span>' for s in result["Missing_Skills"]]),
            unsafe_allow_html=True
        )
    else:
        st.success("No major missing skills found.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Profile Strength Radar")

    scores = {
        "Skills": result["Skill_Match_Score"],
        "Projects": result["Project_Score"],
        "Experience": result["Experience_Score"],
        "Education": result["Education_Score"]
    }

    st.plotly_chart(
        radar_chart(scores),
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🤖 AI Job Fit Review")

    if st.button("Generate AI Job Fit Review", use_container_width=True):
        with st.spinner("Gemini AI is reviewing job fit..."):
            ai_review = ai_resume_review(resume_text, job_description)

        st.markdown(ai_review)

        report_text = f"""
# SkillLens AI Job Matching Report

## Job Match Result

Final Match Score: {score}%

Verdict: {verdict}

Skill Match Score: {result['Skill_Match_Score']}%

## Matched Skills
{", ".join(result['Matched_Skills'])}

## Missing Skills
{", ".join(result['Missing_Skills'])}

## AI Job Fit Review

{ai_review}
"""

        st.download_button(
            "📥 Download Job Match Report",
            report_text,
            "skilllens_job_match_report.md",
            "text/markdown",
            use_container_width=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Upload your resume and paste job description to start matching.")