from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, job_description):

    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer(stop_words="english")

    matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])

    return round(similarity[0][0] * 100, 2)


def calculate_resume_level(score):

    if score >= 90:
        return "Excellent"

    elif score >= 80:
        return "Very Good"

    elif score >= 70:
        return "Good"

    elif score >= 60:
        return "Average"

    else:
        return "Needs Improvement"


def hybrid_ats_engine(
    resume_text,
    job_description,
    resume_skills,
    job_skills,
    clean_text
):

    resume_clean = clean_text(resume_text)

    matched_skills = sorted(
        list(set(resume_skills) & set(job_skills))
    )

    missing_skills = sorted(
        list(set(job_skills) - set(resume_skills))
    )

    if len(job_skills):

        skill_match_score = (
            len(matched_skills) /
            len(job_skills)
        ) * 100

    else:

        skill_match_score = 0

    similarity_score = calculate_similarity(
        resume_text,
        job_description
    )

    similarity_score = max(
        similarity_score,
        skill_match_score
    )

    project_keywords = [
        "project",
        "developed",
        "built",
        "created",
        "deployment",
        "dashboard",
        "api",
        "model"
    ]

    experience_keywords = [
        "intern",
        "experience",
        "developer",
        "engineer",
        "company",
        "remote",
        "agile"
    ]

    education_keywords = [
        "b.tech",
        "college",
        "cgpa",
        "degree",
        "university"
    ]

    project_score = min(
        sum(
            word in resume_clean
            for word in project_keywords
        ) * 12.5,
        100
    )

    experience_score = min(
        sum(
            word in resume_clean
            for word in experience_keywords
        ) * 15,
        100
    )

    education_score = min(
        sum(
            word in resume_clean
            for word in education_keywords
        ) * 20,
        100
    )

    final_score = (

        0.50 * skill_match_score +

        0.20 * similarity_score +

        0.15 * project_score +

        0.10 * experience_score +

        0.05 * education_score

    )

    return {

        "Final_ATS_Score": round(final_score, 2),

        "Skill_Match_Score": round(skill_match_score, 2),

        "Similarity_Score": round(similarity_score, 2),

        "Project_Score": round(project_score, 2),

        "Experience_Score": round(experience_score, 2),

        "Education_Score": round(education_score, 2),

        "Matched_Skills": matched_skills,

        "Missing_Skills": missing_skills,

        "Resume_Level": calculate_resume_level(
            final_score
        )

    }