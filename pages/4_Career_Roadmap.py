import streamlit as st
import time

st.set_page_config(
    page_title="Career Roadmap",
    page_icon="🗺️",
    layout="wide"
)

st.markdown("""
<style>

#MainMenu, footer, header{
visibility:hidden;
}

.stApp{
background:
radial-gradient(circle at top left,rgba(59,130,246,.25),transparent 35%),
radial-gradient(circle at top right,rgba(139,92,246,.25),transparent 35%),
linear-gradient(135deg,#020617,#0f172a);
color:white;
}

.hero,.card{
background:rgba(15,23,42,.82);
padding:30px;
border-radius:25px;
border:1px solid rgba(255,255,255,.12);
box-shadow:0 20px 60px rgba(0,0,0,.35);
}

.title{
font-size:56px;
font-weight:900;
background:linear-gradient(90deg,#38bdf8,#8b5cf6,#22c55e);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
font-size:18px;
color:#cbd5e1;
}

.step{
padding:20px;
margin-top:15px;
border-radius:18px;
background:#111827;
border-left:6px solid #38bdf8;
}

button{
border-radius:12px!important;
}

</style>
""",unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<div class="title">
🗺️ AI Career Roadmap
</div>

<div class="subtitle">

Generate a personalized 30 / 60 / 90 Day Roadmap
to crack placements and become an industry-ready engineer.

</div>

</div>
""",unsafe_allow_html=True)

st.write("")

career=st.selectbox(
"🎯 Select Your Career Goal",
[
"Machine Learning Engineer",
"Data Scientist",
"AI Engineer",
"Software Engineer",
"Backend Developer"
]
)

level=st.selectbox(
"📈 Current Level",
[
"Beginner",
"Intermediate",
"Advanced"
]
)

generate=st.button(
"🚀 Generate AI Roadmap",
use_container_width=True
)

if generate:

    with st.spinner("SkillLens AI is preparing your roadmap..."):
        time.sleep(2)

    st.success("Roadmap Generated Successfully!")

    st.write("")

    col1,col2,col3=st.columns(3)

    with col1:

        st.markdown("""
<div class="card">

## 📅 First 30 Days

<div class="step">
✅ Master Python
</div>

<div class="step">
✅ DSA Arrays + Strings
</div>

<div class="step">
✅ Pandas & NumPy
</div>

<div class="step">
✅ Resume Improvement
</div>

</div>
""",unsafe_allow_html=True)

    with col2:

        st.markdown("""
<div class="card">

## 📅 Next 60 Days

<div class="step">
✅ Build 2 ML Projects
</div>

<div class="step">
✅ Streamlit Deployment
</div>

<div class="step">
✅ Docker Basics
</div>

<div class="step">
✅ AWS Basics
</div>

</div>
""",unsafe_allow_html=True)

    with col3:

        st.markdown("""
<div class="card">

## 📅 Final 90 Days

<div class="step">
✅ Mock Interviews
</div>

<div class="step">
✅ LeetCode Daily
</div>

<div class="step">
✅ Apply 200+ Jobs
</div>

<div class="step">
✅ LinkedIn Optimization
</div>

</div>
""",unsafe_allow_html=True)

    st.write("")

    st.markdown("## 🏆 Recommended Certifications")

    st.success("""
• AWS Cloud Practitioner

• Google AI Essentials

• IBM Machine Learning

• DeepLearning.AI

• TensorFlow Developer
""")

    st.write("")

    st.markdown("## 💻 Recommended Projects")

    st.info("""
• Resume Analyzer

• Fake News Detection

• House Price Prediction

• AI Chatbot

• Image Classification

• Object Detection
""")

    st.write("")

    st.markdown("## 📚 Free Learning Resources")

    st.warning("""
• freeCodeCamp

• CampusX

• Krish Naik

• CodeBasics

• Coursera Audit

• Kaggle Learn
""")

    roadmap=f"""
Career Goal : {career}

Current Level : {level}

30 Days
Python
DSA
Pandas
Resume

60 Days
Projects
Docker
AWS
Deployment

90 Days
Interviews
Applications
LinkedIn
Networking
"""

    st.download_button(
        "📥 Download Career Roadmap",
        roadmap,
        "career_roadmap.txt",
        use_container_width=True
    )

else:

    st.info("Select your career goal and click Generate AI Roadmap.")