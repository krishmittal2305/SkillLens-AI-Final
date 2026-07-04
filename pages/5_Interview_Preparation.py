import streamlit as st

st.set_page_config(
    page_title="Interview Preparation",
    page_icon="🎤",
    layout="wide"
)

st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden;}

.stApp {
    background:
    radial-gradient(circle at top left,rgba(59,130,246,.25),transparent 35%),
    radial-gradient(circle at top right,rgba(139,92,246,.25),transparent 35%),
    linear-gradient(135deg,#020617,#0f172a);
    color:white;
}

.hero,.card {
    background:rgba(15,23,42,.82);
    padding:30px;
    border-radius:25px;
    border:1px solid rgba(255,255,255,.12);
    box-shadow:0 20px 60px rgba(0,0,0,.35);
}

.title {
    font-size:56px;
    font-weight:900;
    background:linear-gradient(90deg,#38bdf8,#8b5cf6,#22c55e);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle {
    font-size:18px;
    color:#cbd5e1;
    line-height:1.7;
}

.q {
    padding:16px;
    margin-top:12px;
    border-radius:16px;
    background:#111827;
    border-left:5px solid #38bdf8;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="title">🎤 AI Interview Preparation</div>
    <div class="subtitle">
        Generate role-based HR, technical, coding, and project interview questions
        to prepare confidently for placements and internships.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

c1, c2 = st.columns(2)

with c1:
    role = st.selectbox(
        "🎯 Select Target Role",
        [
            "Machine Learning Engineer",
            "Data Scientist",
            "AI Engineer",
            "Software Engineer",
            "Backend Developer"
        ]
    )

with c2:
    difficulty = st.selectbox(
        "📚 Select Difficulty",
        ["Easy", "Medium", "Hard"]
    )

generate = st.button("🚀 Generate Interview Kit", use_container_width=True)

if generate:

    st.success("Interview preparation kit generated successfully!")

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div class="card">

## 🧑‍💼 HR Questions

<div class="q">Tell me about yourself.</div>
<div class="q">Why should we hire you?</div>
<div class="q">What are your strengths and weaknesses?</div>
<div class="q">Tell me about your most challenging project.</div>
<div class="q">Where do you see yourself in 5 years?</div>

</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
<div class="card">

## 🧠 Technical Questions for {role}

<div class="q">Explain your strongest project in detail.</div>
<div class="q">Explain OOP concepts with examples.</div>
<div class="q">Explain REST API and how you used it.</div>
<div class="q">Explain SQL joins.</div>
<div class="q">Explain Git and GitHub workflow.</div>

</div>
""", unsafe_allow_html=True)

    st.write("")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
<div class="card">

## 🤖 Machine Learning Questions

<div class="q">What is overfitting and underfitting?</div>
<div class="q">Explain train-test split.</div>
<div class="q">What is precision, recall and F1-score?</div>
<div class="q">Explain Random Forest.</div>
<div class="q">What is feature engineering?</div>

</div>
""", unsafe_allow_html=True)

    with col4:
        st.markdown("""
<div class="card">

## 💻 Coding Questions

<div class="q">Find maximum subarray sum.</div>
<div class="q">Reverse a linked list.</div>
<div class="q">Find duplicates in an array.</div>
<div class="q">Search in rotated sorted array.</div>
<div class="q">Two Sum problem.</div>

</div>
""", unsafe_allow_html=True)

    st.write("")

    st.markdown("""
<div class="card">

## ⭐ Interview Strategy

<div class="q">Prepare a 60-second introduction.</div>
<div class="q">Keep 2 strong projects ready for explanation.</div>
<div class="q">Revise DSA basics daily.</div>
<div class="q">Practice SQL and OOP concepts.</div>
<div class="q">Prepare STAR format answers for HR questions.</div>

</div>
""", unsafe_allow_html=True)

    interview_sheet = f"""
SkillLens AI Interview Kit

Target Role: {role}
Difficulty: {difficulty}

HR Questions:
1. Tell me about yourself.
2. Why should we hire you?
3. What are your strengths and weaknesses?
4. Tell me about your most challenging project.
5. Where do you see yourself in 5 years?

Technical Questions:
1. Explain your strongest project.
2. Explain OOP concepts.
3. Explain REST API.
4. Explain SQL joins.
5. Explain Git workflow.

ML Questions:
1. Overfitting and underfitting.
2. Train-test split.
3. Precision, recall, F1-score.
4. Random Forest.
5. Feature engineering.

Coding Questions:
1. Maximum subarray sum.
2. Reverse linked list.
3. Find duplicates.
4. Search rotated sorted array.
5. Two Sum.
"""

    st.download_button(
        "📥 Download Interview Kit",
        interview_sheet,
        "interview_preparation_kit.txt",
        use_container_width=True
    )

else:
    st.info("Select role and difficulty, then generate your interview kit.")