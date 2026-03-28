import streamlit as st
import pandas as pd
from src.analyzer import analyze_resume
from utils.file_handler import extract_text_from_pdf

st.set_page_config(page_title="Skill Gap Analyzer", layout="centered")

st.title("📄 Resume Skill Gap Analyzer")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# OR manual input
resume_text_input = st.text_area("Or Paste Resume Text")

job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    # Load skills dataset
    skills_df = pd.read_csv("data/skills_dataset.csv")
    skills_list = skills_df["skills"].tolist()

    # Extract resume text
    if uploaded_file:
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = resume_text_input

    if not resume_text or not job_desc:
        st.warning("Please provide both resume and job description")
    else:
        result = analyze_resume(resume_text, job_desc, skills_list)

        st.subheader(f" Match Score: {result['match_score']}%")

        st.subheader("✅ Resume Skills")
        st.write(result["resume_skills"])

        st.subheader("📌 Job Skills Required")
        st.write(result["job_skills"])

        st.subheader("❌ Missing Skills")
        if result["missing_skills"]:
            st.write(result["missing_skills"])
        else:
            st.success("You match all required skills! 🎉")
