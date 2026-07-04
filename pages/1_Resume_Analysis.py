
import streamlit as st
import tempfile, os, sys
sys.path.append(os.getcwd())
from modules.parser import extract_resume_text, clean_text
from modules.skills import skills_database, smart_extract_skills, flatten_skill_map
from modules.ats import hybrid_ats_engine
from modules.charts import ats_gauge, skill_pie, skills_bar, radar_chart
try:
    from modules.ai import ai_resume_review
except Exception:
    ai_resume_review = None

st.set_page_config(page_title="Resume Analysis", page_icon="📄", layout="wide")
st.markdown('\n<style>\n#MainMenu, header, footer {visibility:hidden;}\n.stApp {background:radial-gradient(circle at top left,rgba(59,130,246,.25),transparent 35%),radial-gradient(circle at top right,rgba(139,92,246,.25),transparent 35%),linear-gradient(135deg,#020617,#0f172a); color:white;}\n.block-container {max-width:1400px; padding-top:2rem;}\n.hero,.card,.upload-box {background:rgba(15,23,42,.78);border:1px solid rgba(255,255,255,.12);border-radius:28px;padding:30px;box-shadow:0 25px 70px rgba(0,0,0,.35);}\n.title {font-size:52px;font-weight:950;background:linear-gradient(90deg,#38bdf8,#8b5cf6,#22c55e);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}\n.subtitle {color:#cbd5e1;font-size:18px;line-height:1.7;}\n.metric-card {padding:24px;border-radius:24px;background:rgba(15,23,42,.85);border:1px solid rgba(56,189,248,.25);text-align:center;}\n.metric-card h2 {font-size:42px;color:#38bdf8;margin:0;}\n.metric-card p {color:#cbd5e1;}\n.skill-chip {display:inline-block;padding:9px 15px;margin:6px;border-radius:999px;background:rgba(56,189,248,.14);border:1px solid rgba(56,189,248,.35);color:#bae6fd;font-weight:700;}\n.missing-chip {display:inline-block;padding:9px 15px;margin:6px;border-radius:999px;background:rgba(239,68,68,.14);border:1px solid rgba(239,68,68,.35);color:#fecaca;font-weight:700;}\ndiv.stButton > button {border-radius:16px;padding:12px 20px;background:linear-gradient(90deg,#2563eb,#7c3aed);color:white;border:0;font-weight:900;}\n</style>\n', unsafe_allow_html=True)
st.page_link("app.py", label="← Back to Home")
st.markdown('<div class="hero"><div class="title">Resume Intelligence Dashboard</div><div class="subtitle">Upload your resume, compare it with a target job description, calculate Hybrid ATS score, detect skills and generate AI recruiter feedback.</div></div>', unsafe_allow_html=True)
st.write("")
left, right = st.columns([1,1])
with left:
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    st.subheader("📄 Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])
    st.markdown('</div>', unsafe_allow_html=True)
with right:
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    st.subheader("🎯 Target Job Description")
    job_description = st.text_area("Paste Job Description", height=220, value="""Machine Learning Engineer

Requirements:
Python, Machine Learning, SQL, Pandas, NumPy, Scikit-learn, Git, GitHub, REST API, Docker, AWS, Streamlit, Data Structures, Algorithms.

Responsibilities:
Build ML models, deploy APIs, analyze datasets, collaborate with teams, optimize ML pipelines, and create production-ready AI solutions.""")
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("🚀 Analyze Resume", use_container_width=True):
    if uploaded_file is None:
        st.error("Please upload a resume PDF first."); st.stop()
    with st.spinner("SkillLens AI is analyzing your resume..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read()); temp_path=tmp.name
        resume_text = extract_resume_text(temp_path)
        resume_skill_map = smart_extract_skills(resume_text, skills_database)
        resume_skills = flatten_skill_map(resume_skill_map)
        job_skill_map = smart_extract_skills(job_description, skills_database)
        job_skills = flatten_skill_map(job_skill_map)
        result = hybrid_ats_engine(resume_text, job_description, resume_skills, job_skills, clean_text)
        st.session_state["resume_text"] = resume_text
        st.session_state["job_description"] = job_description
        st.session_state["analysis_result"] = result
    st.success("Analysis completed successfully.")

if "analysis_result" in st.session_state:
    result=st.session_state["analysis_result"]
    c1,c2,c3,c4=st.columns(4)
    cards=[(f"{result['Final_ATS_Score']}%","Hybrid ATS Score"),(f"{result['Skill_Match_Score']}%","Skill Match"),(len(result['Matched_Skills']),"Matched Skills"),(result['Resume_Level'],"Resume Level")]
    for c,(v,l) in zip([c1,c2,c3,c4],cards):
        with c: st.markdown(f'<div class="metric-card"><h2>{v}</h2><p>{l}</p></div>', unsafe_allow_html=True)
    st.write("")
    g1,g2=st.columns(2)
    with g1: st.plotly_chart(ats_gauge(result["Final_ATS_Score"]), use_container_width=True)
    with g2: st.plotly_chart(skill_pie(result["Matched_Skills"], result["Missing_Skills"]), use_container_width=True)
    st.markdown('<div class="card"><h3>✅ Matched Skills</h3>' + ''.join([f'<span class="skill-chip">{s}</span>' for s in result["Matched_Skills"]]) + '</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="card"><h3>⚠️ Missing Skills</h3>' + (''.join([f'<span class="missing-chip">{s}</span>' for s in result["Missing_Skills"]]) or '<p>No major missing skills found.</p>') + '</div>', unsafe_allow_html=True)
    st.write("")
    chart1,chart2=st.columns(2)
    with chart1:
        if result["Matched_Skills"]: st.plotly_chart(skills_bar(result["Matched_Skills"]), use_container_width=True)
    with chart2:
        st.plotly_chart(radar_chart({"Skills":result["Skill_Match_Score"],"Projects":result["Project_Score"],"Experience":result["Experience_Score"],"Education":result["Education_Score"]}), use_container_width=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🤖 AI Recruiter Review")
    if st.button("Generate AI Recruiter Review", use_container_width=True):
        if ai_resume_review is None:
            st.error("Gemini module is not available.")
        else:
            with st.spinner("Gemini AI is reviewing your resume..."):
                try:
                    review = ai_resume_review(st.session_state["resume_text"], st.session_state["job_description"])
                    st.session_state["ai_review"] = review
                except Exception as e:
                    st.error(f"AI review failed: {e}")
    if "ai_review" in st.session_state:
        st.markdown(st.session_state["ai_review"])
        report=f"""# SkillLens AI Resume Report

ATS Score: {result['Final_ATS_Score']}%

Resume Level: {result['Resume_Level']}

Matched Skills: {', '.join(result['Matched_Skills'])}

Missing Skills: {', '.join(result['Missing_Skills'])}

## AI Review
{st.session_state['ai_review']}"""
        st.download_button("📥 Download Report", report, "skilllens_resume_report.md", "text/markdown", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Upload your resume and click Analyze Resume to start.")
