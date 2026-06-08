def honeypot_penalty(candidate):

    s = candidate["redrob_signals"]

    penalty = 0

    if s["recruiter_response_rate"] < 0.10:
        penalty += 15

    if s["interview_completion_rate"] < 0.20:
        penalty += 15

    if s["profile_completeness_score"] < 40:
        penalty += 10

    return penalty