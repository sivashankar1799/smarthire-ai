# src/main.py

import os
import numpy as np

from parser import load_job_description, load_candidates
from embeddings import candidate_text, embed
from faiss_index import build_index, search
from jd_analyzer import extract_skills
from skill_match import score_skills
from startup_fit import startup_score
from scoring import behavioral_score
from honeypot import honeypot_penalty
from exporter import export


def is_ai_candidate(candidate):

    title = candidate["profile"].get(
        "current_title",
        ""
    ).lower()

    skills = []

    for skill in candidate.get(
        "skills",
        []
    ):
        skills.append(
            skill["name"].lower()
        )

    ai_titles = [

        "ai engineer",
        "machine learning engineer",
        "ml engineer",
        "data scientist",
        "nlp engineer",
        "research engineer",
        "deep learning engineer",
        "artificial intelligence"
    ]

    for role in ai_titles:

        if role in title:
            return True

    ai_skills = [

        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "nlp",
        "llm",
        "rag"
    ]

    matches = 0

    for skill in skills:

        if skill in ai_skills:
            matches += 1

    return matches >= 3


def ai_relevance_score(candidate):

    text = ""

    profile = candidate["profile"]

    text += profile.get(
        "current_title",
        ""
    ).lower()

    text += " "

    text += profile.get(
        "summary",
        ""
    ).lower()

    for skill in candidate.get(
        "skills",
        []
    ):
        text += " "
        text += skill["name"].lower()

    keywords = [

        "ai",
        "machine learning",
        "ml",
        "deep learning",
        "nlp",
        "llm",
        "transformer",
        "pytorch",
        "tensorflow",
        "rag",
        "vector",
        "embedding",
        "data science"
    ]

    score = 0

    for keyword in keywords:

        if keyword in text:
            score += 10

    return score

def calculate_availability(signals):

    score = 0

    if signals.get("open_to_work_flag", False):
        score += 50

    notice = signals.get(
        "notice_period_days",
        180
    )

    if notice <= 30:
        score += 30
    elif notice <= 60:
        score += 15

    if signals.get(
        "verified_email",
        False
    ):
        score += 10

    if signals.get(
        "verified_phone",
        False
    ):
        score += 10

    return min(score, 100)


def ai_role_bonus(candidate):

    title = (
        candidate["profile"]
        .get("current_title", "")
        .lower()
    )

    ai_roles = [

        "ai engineer",
        "machine learning engineer",
        "ml engineer",
        "data scientist",
        "research engineer",
        "nlp engineer",
        "deep learning engineer",
        "artificial intelligence"
    ]

    for role in ai_roles:

        if role in title:
            return 20

    return 0


def non_ai_penalty(candidate):

    title = (
        candidate["profile"]
        .get("current_title", "")
        .lower()
    )

    bad_roles = [

        "hr",
        "civil",
        "mechanical",
        "graphic designer",
        "sales",
        "marketing"
    ]

    for role in bad_roles:

        if role in title:
            return 25

    return 0


def generate_reasoning(
    candidate,
    semantic,
    skill_score_value,
    behavior
):

    profile = candidate["profile"]

    return (
        f"Experience={profile['years_of_experience']} years; "
        f"Current Role={profile['current_title']}; "
        f"Semantic={semantic:.2f}; "
        f"Skill={skill_score_value:.2f}; "
        f"Behavior={behavior:.2f}"
    )


def main():

    print("=" * 60)
    print("SMARTHIRE AI")
    print("=" * 60)

    ROOT_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    DATA_DIR = os.path.join(
        ROOT_DIR,
        "data"
    )

    MODELS_DIR = os.path.join(
        ROOT_DIR,
        "models"
    )

    os.makedirs(
        MODELS_DIR,
        exist_ok=True
    )

    JD_FILE = os.path.join(
        DATA_DIR,
        "job_description.docx"
    )

    CANDIDATES_FILE = os.path.join(
        DATA_DIR,
        "candidates.jsonl"
    )

    OUTPUT_FILE = os.path.join(
        DATA_DIR,
        "submission.csv"
    )

    EMBEDDING_FILE = os.path.join(
        MODELS_DIR,
        "candidate_embeddings.npy"
    )

    print("\nLoading Job Description...")
    jd = load_job_description(
        JD_FILE
    )

    print("Loading Candidates...")
    candidates = load_candidates(
        CANDIDATES_FILE
    )

    print(
        f"Loaded {len(candidates)} candidates"
    )

    # ----------------------------------
    # TEST MODE
    # ----------------------------------

    TEST_MODE = False

    if TEST_MODE:

        candidates = candidates[:5000]

        print(
            f"TEST MODE ACTIVE "
            f"({len(candidates)} candidates)"
        )

    # ----------------------------------
    # JD SKILLS
    # ----------------------------------

    print("\nExtracting JD Skills...")

    jd_skills = extract_skills(jd)

    print(jd_skills)

    # ----------------------------------
    # CANDIDATE TEXTS
    # ----------------------------------

    print(
        "\nPreparing Candidate Texts..."
    )

    candidate_texts = [

        candidate_text(c)

        for c in candidates
    ]

    # ----------------------------------
    # EMBEDDINGS
    # ----------------------------------

    if os.path.exists(
        EMBEDDING_FILE
    ):

        print(
            "\nLoading Cached Embeddings..."
        )

        candidate_embeddings = np.load(
            EMBEDDING_FILE
        )

    else:

        print(
            "\nGenerating Embeddings..."
        )

        candidate_embeddings = embed(
            candidate_texts
        )

        np.save(
            EMBEDDING_FILE,
            candidate_embeddings
        )

        print(
            "Embeddings Saved."
        )

    # ----------------------------------
    # JD EMBEDDING
    # ----------------------------------

    print(
        "\nGenerating JD Embedding..."
    )

    jd_embedding = embed(
        [jd]
    )[0]

    # ----------------------------------
    # FAISS
    # ----------------------------------

    print(
        "\nBuilding FAISS Index..."
    )

    index = build_index(
        candidate_embeddings
    )

    print(
        "\nSearching Top Candidates..."
    )

    similarities, ids = search(
        index,
        jd_embedding,
        top_k=min(
            1000,
            len(candidates)
        )
    )

    filtered_candidates = []

    for candidate in candidates:

        if is_ai_candidate(candidate):
            filtered_candidates.append(candidate)

    candidates = filtered_candidates

    print(
        f"AI Candidates: {len(candidates)}"
    )
    print("\nSample AI Candidates:")

    for c in candidates[:10]:

        print(
            c["profile"]["current_title"]
        )
    # ----------------------------------
    # SCORING
    # ----------------------------------

    ranked = []

    print(
        "\nScoring Candidates..."
    )

    for similarity, idx in zip(
    similarities,
    ids
    ):

        if idx < 0:
            continue

        if idx >= len(candidates):
            continue

        candidate = candidates[idx]

        candidate = candidates[idx]

        skill_score_value = score_skills(
            candidate,
            jd_skills
        )

        startup = startup_score(
            candidate
        )

        behavior = behavioral_score(
            candidate["redrob_signals"]
        )

        availability = calculate_availability(
            candidate["redrob_signals"]
        )

        bonus = ai_role_bonus(
            candidate
        )

        role_penalty = non_ai_penalty(
            candidate
        )

        honeypot = honeypot_penalty(
            candidate
        )

        relevance = ai_relevance_score(
    candidate
)

        final_score = (
        similarity * 0.50
        + skill_score_value * 0.20
        + startup * 0.10
        + behavior * 0.10
        + availability * 0.10
    )
        
        #final_score = final_score / 20
        final_score = round(final_score, 2)
        

        reasoning = generate_reasoning(

            candidate,

            similarity * 100,

            skill_score_value,

            behavior
        )

        ranked.append({

            "candidate_id":
                candidate["candidate_id"],

            "score":
                round(
                    float(final_score),
                    4
                ),

            "reasoning":
                reasoning
        })

    # ----------------------------------
    # SORT
    # ----------------------------------

    ranked.sort(

        key=lambda x: (

            -x["score"],

            x["candidate_id"]
        )
    )

    top100 = ranked[:100]

    print(
        f"\nSelected "
        f"{len(top100)} candidates"
    )

    # ----------------------------------
    # EXPORT
    # ----------------------------------

    export(
        top100,
        OUTPUT_FILE
    )

    print(
        "\nSubmission Generated:"
    )

    print(
        OUTPUT_FILE
    )

    print(
        "\nDone."
    )


if __name__ == "__main__":
    main()
