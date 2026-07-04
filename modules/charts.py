import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def ats_gauge(score):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "%"},
            title={"text": "Hybrid ATS Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#22c55e"},
                "steps": [
                    {"range": [0, 40], "color": "#ef4444"},
                    {"range": [40, 70], "color": "#f59e0b"},
                    {"range": [70, 100], "color": "#22c55e"},
                ],
            },
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=350,
        margin=dict(l=20, r=20, t=50, b=20),
    )

    return fig


def skill_pie(matched, missing):
    labels = ["Matched Skills", "Missing Skills"]
    values = [len(matched), len(missing)]

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.55,
    )

    fig.update_layout(
        template="plotly_dark",
        height=380,
        showlegend=True,
    )

    return fig


def skills_bar(matched):
    df = pd.DataFrame({
        "Skill": matched,
        "Score": [100] * len(matched)
    })

    fig = px.bar(
        df,
        x="Skill",
        y="Score",
    )

    fig.update_layout(
        template="plotly_dark",
        height=400,
        showlegend=False,
    )

    return fig


def radar_chart(scores):

    categories = list(scores.keys())
    values = list(scores.values())

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself'
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100]
            )
        ),
        template="plotly_dark",
        height=430
    )

    return fig