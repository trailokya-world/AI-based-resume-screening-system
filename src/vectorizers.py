from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def cosine_score(processed_text,job_description):


    embedding_model = SentenceTransformer("BAAI/bge-base-en-v1.5")

    resume_embedding = embedding_model.encode(
        [processed_text],
        normalize_embeddings=True
    )
    jd_embedding = embedding_model.encode(
        [job_description],
        normalize_embeddings=True
    )

    score = cosine_similarity(resume_embedding, jd_embedding)[0][0]

    return score