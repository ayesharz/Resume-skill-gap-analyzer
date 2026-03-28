from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume, job_desc):
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform([resume, job_desc])

    similarity_score = cosine_similarity(
        tfidf_matrix[0:1], tfidf_matrix[1:2]
    )[0][0]

    return round(similarity_score * 100, 2)
