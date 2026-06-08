def startup_score(candidate):

    score = 0

    for job in candidate["career_history"]:

        size = job["company_size"]

        if size in [
            "1-10",
            "11-50",
            "51-200"
        ]:
            score += 15

        title = job["title"].lower()

        if (
            "founding" in title or
            "lead" in title or
            "principal" in title
        ):
            score += 10

    return min(score,100)