import numpy as np
from scoring import behavioral_score

def rank_candidates(
    candidates,
    semantic_scores
):

    results = []

    for cand,sim in zip(
        candidates,
        semantic_scores
    ):

        behavior = behavioral_score(
            cand["redrob_signals"]
        )

        final_score = (
            sim * 85
            + behavior * 0.15
        )

        results.append(
            (
                cand["candidate_id"],
                final_score,
                cand
            )
        )

    results.sort(
        key=lambda x:x[1],
        reverse=True
    )

    return results[:100]