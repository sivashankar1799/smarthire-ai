PROFICIENCY = {

    "beginner":0.25,
    "intermediate":0.50,
    "advanced":0.75,
    "expert":1.00
}

def score_skills(
    candidate,
    jd_skills
):

    total = 0

    matched = 0

    for skill in candidate["skills"]:

        name = skill["name"].lower()

        if name in jd_skills:

            matched += 1

            total += (
                PROFICIENCY[
                    skill["proficiency"]
                ]
            )

    if len(jd_skills) == 0:
        return 0

    return (
        total / len(jd_skills)
    ) * 100