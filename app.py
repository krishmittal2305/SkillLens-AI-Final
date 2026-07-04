import streamlit as st

st.set_page_config(page_title="SkillLens AI", page_icon="🧠", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}
[data-testid="stSidebar"] {display:none;}
.block-container {max-width:100%; padding:0;}
.stApp {background:radial-gradient(circle at 12% 10%, rgba(56,189,248,0.22), transparent 28%),radial-gradient(circle at 88% 16%, rgba(139,92,246,0.32), transparent 32%),radial-gradient(circle at 50% 90%, rgba(34,197,94,0.10), transparent 30%),linear-gradient(135deg,#020617,#0f172a 48%,#160a37); color:white;}
.main-wrap {width:92%; margin:auto; padding:34px 0 60px 0;}
.navbar {display:flex; align-items:center; justify-content:space-between; gap:22px; padding:24px 34px; border-radius:32px; background:rgba(15,23,42,0.78); border:1px solid rgba(148,163,184,0.22); box-shadow:0 25px 75px rgba(0,0,0,.36); backdrop-filter:blur(18px);}
.logo {font-size:38px; font-weight:950; letter-spacing:-1.5px; background:linear-gradient(90deg,#38bdf8,#8b5cf6,#22c55e); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
.nav-sub {font-size:15px; font-weight:800; color:#94a3b8; margin-top:2px;}
.nav-section {width:92%; margin:14px auto 0 auto;}
div[data-testid="stPageLink"] a {background:rgba(15,23,42,0.72) !important; border:1px solid rgba(148,163,184,0.22) !important; border-radius:18px !important; padding:13px 18px !important; text-decoration:none !important; color:#dbeafe !important; font-weight:900 !important; box-shadow:0 12px 30px rgba(0,0,0,.18); justify-content:center !important; transition:.22s ease !important;}
div[data-testid="stPageLink"] a:hover {background:linear-gradient(90deg,#2563eb,#7c3aed) !important; color:white !important; transform:translateY(-2px); box-shadow:0 16px 45px rgba(124,58,237,.32);}
.hero {margin-top:78px; display:grid; grid-template-columns:1.05fr .95fr; gap:70px; align-items:center;}
.badge {display:inline-block; padding:12px 22px; border-radius:999px; color:#7dd3fc; font-size:18px; font-weight:900; background:rgba(56,189,248,.14); border:1px solid rgba(56,189,248,.38);}
.hero-title {margin-top:34px; font-size:92px; line-height:.98; letter-spacing:-5px; font-weight:950; background:linear-gradient(90deg,#38bdf8,#93c5fd,#a78bfa); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
.hero-desc {margin-top:34px; max-width:850px; color:#dbeafe; font-size:26px; line-height:1.65;}
.hero-actions {display:flex; gap:20px; margin-top:42px; flex-wrap:wrap;}
.cta-primary, .cta-secondary {display:inline-block; padding:18px 34px; border-radius:20px; font-size:19px; font-weight:950; text-decoration:none; color:white;}
.cta-primary {background:linear-gradient(90deg,#2563eb,#7c3aed); box-shadow:0 18px 55px rgba(124,58,237,.42);}
.cta-secondary {background:rgba(15,23,42,.72); border:1px solid rgba(148,163,184,.28);}
.ai-panel {padding:38px; border-radius:36px; background:rgba(15,23,42,.78); border:1px solid rgba(148,163,184,.22); box-shadow:0 35px 100px rgba(0,0,0,.45);}
.score-card {padding:36px; border-radius:32px; background:rgba(30,41,59,.82); border:1px solid rgba(56,189,248,.35);}
.score-label {color:#94a3b8; font-size:22px; font-weight:850;}
.score {margin-top:10px; font-size:82px; font-weight:950; color:#22c55e;}
.progress {margin-top:20px; height:15px; border-radius:999px; background:#1e293b; overflow:hidden;}
.progress-fill {height:100%; width:92%; border-radius:999px; background:linear-gradient(90deg,#22c55e,#38bdf8);}
.mini-grid {margin-top:26px; display:grid; grid-template-columns:repeat(2,1fr); gap:22px;}
.mini-card {padding:26px; border-radius:26px; background:rgba(2,6,23,.72); border:1px solid rgba(148,163,184,.16);}
.mini-card h3 {margin:0; color:#38bdf8; font-size:38px; font-weight:950;}
.mini-card p {margin:6px 0 0; color:white; font-size:18px; font-weight:750;}
.section-title {margin-top:105px; text-align:center; font-size:52px; font-weight:950; letter-spacing:-1px;}
.section-sub {margin-top:12px; text-align:center; color:#94a3b8; font-size:20px;}
.features {margin-top:46px; display:grid; grid-template-columns:repeat(3,1fr); gap:26px;}
.feature-card {padding:34px; border-radius:32px; min-height:235px; background:rgba(15,23,42,.76); border:1px solid rgba(148,163,184,.18); box-shadow:0 26px 70px rgba(0,0,0,.30); transition:.25s;}
.feature-card:hover {transform:translateY(-8px); border-color:rgba(56,189,248,.70); box-shadow:0 30px 80px rgba(56,189,248,.12);}
.feature-icon {font-size:40px; margin-bottom:14px;}
.feature-card h3 {font-size:25px; font-weight:950; margin:0;}
.feature-card p {margin-top:12px; color:#cbd5e1; font-size:16px; line-height:1.7;}
.tech-stack {margin-top:45px; display:grid; grid-template-columns:repeat(6,1fr); gap:20px;}
.tech {padding:24px; border-radius:24px; text-align:center; background:rgba(15,23,42,.78); border:1px solid rgba(148,163,184,.18); color:#bae6fd; font-weight:950; font-size:18px;}
.workflow {margin-top:45px; display:grid; grid-template-columns:repeat(5,1fr); gap:20px;}
.step {padding:30px; border-radius:28px; text-align:center; background:rgba(15,23,42,.78); border:1px solid rgba(148,163,184,.18);}
.step h3 {color:#22c55e; font-size:32px; font-weight:950; margin:0;}
.step p {color:#e2e8f0; font-size:17px; font-weight:750;}
.footer-box {margin-top:80px; padding:36px; border-radius:30px; text-align:center; color:#cbd5e1; background:rgba(15,23,42,.78); border:1px solid rgba(148,163,184,.18);}
@media(max-width:950px){.hero{grid-template-columns:1fr}.hero-title{font-size:60px}.features{grid-template-columns:1fr}.tech-stack{grid-template-columns:repeat(2,1fr)}.workflow{grid-template-columns:1fr}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-wrap">', unsafe_allow_html=True)
st.markdown('<div class="navbar"><div><div class="logo">SkillLens AI</div><div class="nav-sub">AI Career Intelligence Platform</div></div></div>', unsafe_allow_html=True)

st.markdown('<div class="nav-section">', unsafe_allow_html=True)
nav = st.columns(6)
links = [
    ("pages/1_Resume_Analysis.py", "📄 Resume Analysis"),
    ("pages/2_Resume_Optimizer.py", "✨ Optimizer"),
    ("pages/3_Job_Matching.py", "🎯 Job Matching"),
    ("pages/4_Career_Roadmap.py", "🧭 Roadmap"),
    ("pages/5_Interview_Preparation.py", "🎤 Interview"),
    ("pages/6_Recruiter_Dashboard.py", "👨‍💼 Recruiter"),
]
for col, (page, label) in zip(nav, links):
    with col:
        st.page_link(page, label=label)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div>
        <div class="badge">AI Career Intelligence Platform</div>
        <div class="hero-title">Analyze.<br>Optimize.<br>Get Hired.</div>
        <div class="hero-desc">SkillLens AI helps students analyze resumes, calculate hybrid ATS scores, match job descriptions, detect missing skills, optimize resumes using AI, and generate personalized career roadmaps.</div>
        <div class="hero-actions"><a class="cta-primary" href="#">Start Resume Analysis →</a><a class="cta-secondary" href="#features">View Platform</a></div>
    </div>
    <div class="ai-panel">
        <div class="score-card"><div class="score-label">Hiring Readiness Score</div><div class="score">92%</div><div class="progress"><div class="progress-fill"></div></div></div>
        <div class="mini-grid"><div class="mini-card"><h3>25+</h3><p>Skills Detected</p></div><div class="mini-card"><h3>AI</h3><p>Resume Review</p></div><div class="mini-card"><h3>ATS</h3><p>Hybrid Engine</p></div><div class="mini-card"><h3>90D</h3><p>Career Roadmap</p></div></div>
    </div>
</div>
<div id="features" class="section-title">Built Like a Real AI Product</div><div class="section-sub">Not just a resume analyzer — a complete AI career intelligence platform.</div>
<div class="features">
<div class="feature-card"><div class="feature-icon">📄</div><h3>Resume Intelligence</h3><p>Reads resume PDFs, extracts skills, analyzes experience, projects, education, and career readiness.</p></div>
<div class="feature-card"><div class="feature-icon">🎯</div><h3>Hybrid ATS Engine</h3><p>Combines NLP similarity, skill matching, project score, experience score, and education score.</p></div>
<div class="feature-card"><div class="feature-icon">🤖</div><h3>Gemini AI Review</h3><p>Generates strengths, weaknesses, missing skills, resume improvements, and hiring feedback.</p></div>
<div class="feature-card"><div class="feature-icon">🚀</div><h3>Resume Optimizer</h3><p>Improves summaries, bullet points, ATS keywords, skills section, and project descriptions.</p></div>
<div class="feature-card"><div class="feature-icon">🧭</div><h3>Career Roadmap</h3><p>Creates a personalized 30/60/90-day roadmap for placement and career growth.</p></div>
<div class="feature-card"><div class="feature-icon">👨‍💼</div><h3>Recruiter Dashboard</h3><p>Dashboard for comparing and ranking multiple resumes for a job role.</p></div>
</div>
<div class="section-title">Technology Stack</div><div class="tech-stack"><div class="tech">Python</div><div class="tech">NLP</div><div class="tech">Scikit-learn</div><div class="tech">Gemini API</div><div class="tech">Streamlit</div><div class="tech">Plotly</div></div>
<div class="section-title">How SkillLens AI Works</div><div class="workflow"><div class="step"><h3>01</h3><p>Upload Resume</p></div><div class="step"><h3>02</h3><p>Extract Skills</p></div><div class="step"><h3>03</h3><p>Calculate ATS</p></div><div class="step"><h3>04</h3><p>Generate AI Review</p></div><div class="step"><h3>05</h3><p>Career Roadmap</p></div></div>
<div class="footer-box"><b>Developed by Krish Mittal</b><br><br>A flagship AI + ML project combining Resume Parsing, NLP, Hybrid ATS Scoring, Gemini AI, Career Intelligence, and premium product-style UI.</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
