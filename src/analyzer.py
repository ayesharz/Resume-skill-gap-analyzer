from src.preprocess import clean_text
from src.skill_extractor import extract_skills
from src.similarity import compute_similarity

def analyze_resume(resume_text, job_desc, skills_list):
    # Clean text
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_desc)

    # Extract skills
    resume_skills = extract_skills(resume_clean, skills_list)
    job_skills = extract_skills(job_clean, skills_list)

    # Compute similarity
    score = compute_similarity(resume_clean, job_clean)

    # Find missing skills
    missing_skills = list(set(job_skills) - set(resume_skills))

    return {
        "match_score": score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "missing_skills": missing_skills
    }
