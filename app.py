# Install dependencies
!pip install nltk scikit-learn pandas PyPDF2

# Imports
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

# ---------------------------
# Create dataset
# ---------------------------
skills = [
    "python", "machine learning", "deep learning", "data analysis",
    "sql", "excel", "nlp", "communication", "problem solving",
    "java", "c++", "statistics", "pandas", "numpy"
]

skills_df = pd.DataFrame(skills, columns=["skills"])
skills_list = skills_df["skills"].tolist()

# ---------------------------
# Functions
# ---------------------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in STOPWORDS]
    return " ".join(words)


def extract_skills(text, skills_list):
    text = text.lower()
    return list(set([skill for skill in skills_list if skill in text]))


def compute_similarity(resume, job_desc):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume, job_desc])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)


def analyze_resume(resume_text, job_desc, skills_list):
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_desc)

    resume_skills = extract_skills(resume_clean, skills_list)
    job_skills = extract_skills(job_clean, skills_list)

    score = compute_similarity(resume_clean, job_clean)

    missing_skills = list(set(job_skills) - set(resume_skills))

    return {
        "match_score": score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "missing_skills": missing_skills
    }


# ---------------------------
# OPTIONAL: PDF Reader
# ---------------------------
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# ---------------------------
# TEST INPUT (EDIT THIS)
# ---------------------------
resume = input("Paste Resume Text: ")
job_desc = input("Paste Job Description: ")

# ---------------------------
# RUN ANALYSIS
# ---------------------------
result = analyze_resume(resume, job_desc, skills_list)

# ---------------------------
# OUTPUT
# ---------------------------
print("\n🎯 Match Score:", result["match_score"], "%")
print("\n✅ Resume Skills:", result["resume_skills"])
print("\n📌 Job Skills Required:", result["job_skills"])
print("\n❌ Missing Skills:", result["missing_skills"] if result["missing_skills"] else "None 🎉")
