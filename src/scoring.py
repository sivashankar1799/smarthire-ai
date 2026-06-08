def behavioral_score(signals):

    score = 0

    score += signals["profile_completeness_score"] * 0.10

    score += signals["recruiter_response_rate"] * 100 * 0.25

    score += signals["interview_completion_rate"] * 100 * 0.20

    score += signals["saved_by_recruiters_30d"] * 0.5

    github = signals["github_activity_score"]

    if github > 0:
        score += github * 0.20

    if signals["open_to_work_flag"]:
        score += 10

    return min(score, 100)