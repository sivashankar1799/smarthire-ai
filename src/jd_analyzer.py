TARGET_SKILLS = [

    "python",
    "llm",
    "rag",
    "transformers",
    "pytorch",
    "tensorflow",
    "vector databases",
    "embedding",
    "nlp",
    "machine learning",
    "deep learning",
    "aws",
    "gcp"
]

def extract_skills(jd_text):

    jd = jd_text.lower()

    found = []

    for skill in TARGET_SKILLS:

        if skill in jd:
            found.append(skill)

    return found