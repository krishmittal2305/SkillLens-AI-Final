import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Recruiter Dashboard",
    page_icon="👨‍💼",
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

.metric-card {
    background:rgba(15,23,42,.88);
    border:1px solid rgba(56,189,248,.25);
    border-radius:22px;
    padding:24px;
    text-align:center;
}

.metric-card h2 {
    color:#38bdf8;
    font-size:42px;
    margin:0;
}

.metric-card p {
    color:#cbd5e1;
    margin:8px 0 0 0;
}

.badge-good {
    color:#86efac;
    font-weight:900;
}

.badge-mid {
    color:#fde68a;
    font-weight:900;
}

.badge-low {
    color:#fca5a5;
    font-weight:900;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="title">👨‍💼 Recruiter Dashboard</div>
    <div class="subtitle">
        A recruiter-style hiring dashboard to rank candidates, analyze ATS distribution,
        identify strongest profiles, and export shortlist reports.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

sample_data = {
    "Candidate": [
        "Krish Mittal", "Rahul Sharma", "Aman Verma", "Priya Singh",
        "Rohan Gupta", "Neha Jain", "Arjun Mehta", "Simran Kaur"
    ],
    "Role": [
        "ML Engineer", "Data Scientist", "AI Engineer", "SDE",
        "ML Engineer", "Data Analyst", "Backend Developer", "AI Engineer"
    ],
    "ATS Score": [92, 88, 84, 79, 73, 69, 64, 58],
    "Skill Match": [94, 86, 82, 75, 70, 66, 61, 54],
    "Experience": [1.0, 1.5, 1.2, 0.8, 1.0, 0.6, 0.5, 0.4],
    "Top Skill": [
        "Machine Learning", "Python", "NLP", "DSA",
        "Scikit-learn", "SQL", "FastAPI", "Python"
    ]
}

df = pd.DataFrame(sample_data)

df["Verdict"] = df["ATS Score"].apply(
    lambda x: "Shortlist" if x >= 85 else ("Review" if x >= 70 else "Reject")
)

total_resumes = len(df)
avg_ats = round(df["ATS Score"].mean(), 2)
shortlisted = len(df[df["Verdict"] == "Shortlist"])
review = len(df[df["Verdict"] == "Review"])

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{total_resumes}</h2>
        <p>Total Resumes</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{avg_ats}%</h2>
        <p>Average ATS</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{shortlisted}</h2>
        <p>Shortlisted</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
        <h2>{review}</h2>
        <p>Needs Review</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🏆 Candidate Ranking")

ranked_df = df.sort_values(by="ATS Score", ascending=False).reset_index(drop=True)
ranked_df.index = ranked_df.index + 1

st.dataframe(
    ranked_df,
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

ch1, ch2 = st.columns(2)

with ch1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 ATS Score Distribution")

    fig = px.bar(
        ranked_df,
        x="Candidate",
        y="ATS Score",
        color="ATS Score",
        title="Candidate ATS Scores"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with ch2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎯 Verdict Distribution")

    verdict_count = df["Verdict"].value_counts().reset_index()
    verdict_count.columns = ["Verdict", "Count"]

    fig2 = px.pie(
        verdict_count,
        names="Verdict",
        values="Count",
        hole=0.55,
        title="Hiring Recommendation"
    )

    fig2.update_layout(
        template="plotly_dark",
        height=420
    )

    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🤖 Recruiter Insights")

best_candidate = ranked_df.iloc[0]["Candidate"]
top_skill = df["Top Skill"].mode()[0]
lowest_candidate = ranked_df.iloc[-1]["Candidate"]

st.success(f"Best candidate for shortlist: {best_candidate}")
st.info(f"Most common strong skill: {top_skill}")
st.warning(f"Candidate needing most improvement: {lowest_candidate}")

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

csv = ranked_df.to_csv(index=False)

st.download_button(
    "📥 Download Recruiter Shortlist CSV",
    csv,
    "recruiter_shortlist.csv",
    "text/csv",
    use_container_width=True
)