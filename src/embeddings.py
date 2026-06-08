# src/embeddings.py

from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Embedding model loaded.")


def candidate_text(candidate):

    profile = candidate["profile"]

    text_parts = []

    # Profile
    text_parts.append(
        profile.get("headline", "")
    )

    text_parts.append(
        profile.get("summary", "")
    )

    text_parts.append(
        profile.get("current_title", "")
    )

    text_parts.append(
        profile.get("current_industry", "")
    )

    # Career History
    for job in candidate.get(
        "career_history",
        []
    ):

        text_parts.append(
            job.get("title", "")
        )

        text_parts.append(
            job.get("description", "")
        )

        text_parts.append(
            job.get("industry", "")
        )

    # Skills
    for skill in candidate.get(
        "skills",
        []
    ):

        text_parts.append(
            skill.get("name", "")
        )

    # Certifications
    for cert in candidate.get(
        "certifications",
        []
    ):

        text_parts.append(
            cert.get("name", "")
        )

    return " ".join(text_parts)


def embed(texts):

    return model.encode(
        texts,
        batch_size=128,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )