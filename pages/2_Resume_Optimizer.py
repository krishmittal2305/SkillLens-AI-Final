import streamlit as st
import tempfile
import os
import sys

sys.path.append(os.getcwd())

from modules.parser import extract_resume_text
from modules.ai import optimize_resume

st.set_page_config(page_title="Resume Optimizer", page_icon="✨", layout="wide")

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

.big-btn button {
    background:linear-gradient(90deg,#2563eb,#7c3aed) !important;
    color:white !important;
    border-radius:18px !important;
    height:58px !important;
    font-weight:900 !important;
    border:0 !important;
}

.result-box {
    background:rgba(15,23,42,.86);
    border:1px solid rgba(56,189,248,.22);
    border-radius:26px;
    padding:28px;
    color:#e2e8f0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="title">AI Resume Optimizer</div>
    <div class="subtitle">
        Upload your resume and let SkillLens AI rewrite it into a stronger,
        ATS-friendly, recruiter-focused version with better summary, skills,
        projects, and experience sections.
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
    st.subheader("✨ What SkillLens AI Will Improve")
    st.markdown("""
    - Professional Summary  
    - Project Descriptions  
    - Experience Bullet Points  
    - Technical Skills Section  
    - ATS Keywords  
    - Recruiter Readability  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

st.markdown('<div class="big-btn">', unsafe_allow_html=True)
optimize_btn = st.button("🚀 Optimize My Resume", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

if optimize_btn:

    if uploaded_file is None:
        st.error("Please upload your resume first.")
        st.stop()

    with st.spinner("SkillLens AI is optimizing your resume..."):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        resume_text = extract_resume_text(temp_path)

        optimized_resume = optimize_resume(resume_text)

    st.success("Resume optimized successfully.")

    st.write("")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✨ Optimized Resume Output")
    st.markdown(optimized_resume)
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.download_button(
        "📥 Download Optimized Resume",
        optimized_resume,
        "optimized_resume.md",
        "text/markdown",
        use_container_width=True
    )

else:
    st.info("Upload your resume and click Optimize My Resume.")