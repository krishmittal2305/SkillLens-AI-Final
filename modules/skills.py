import re

# ============================
# Skill Database
# ============================

skills_database = {

    "Programming": [
        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "typescript"
    ],

    "Machine Learning": [
        "machine learning",
        "deep learning",
        "scikit-learn",
        "tensorflow",
        "keras",
        "pytorch",
        "random forest",
        "xgboost",
        "svm",
        "decision tree"
    ],

    "Data Analysis": [
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "plotly"
    ],

    "Database": [
        "sql",
        "mysql",
        "mongodb",
        "postgresql"
    ],

    "Cloud": [
        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes"
    ],

    "Web Development": [
        "flask",
        "fastapi",
        "django",
        "streamlit",
        "react",
        "node.js",
        "rest api"
    ],

    "Tools": [
        "git",
        "github",
        "linux",
        "postman"
    ],

    "Computer Science": [
        "algorithms",
        "data structures",
        "oop",
        "object oriented programming"
    ]
}


# ============================
# Skill Extraction
# ============================

def smart_extract_skills(text, skills_database):

    text = text.lower()

    found = {}

    for category, skills in skills_database.items():

        matched = []

        for skill in skills:

            if re.search(r"\b" + re.escape(skill) + r"\b", text):

                matched.append(skill)

        if matched:

            found[category] = sorted(list(set(matched)))

    return found


# ============================
# Flatten Skills
# ============================

def flatten_skill_map(skill_map):

    skills = []

    for category in skill_map:

        skills.extend(skill_map[category])

    return sorted(list(set(skills)))