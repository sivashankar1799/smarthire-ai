import pandas as pd

def export(top100, output_file):

    rows = []

    rank = 1

    for item in top100:

        rows.append([
            item["candidate_id"],
            rank,
            item["score"],
            item["reasoning"]
        ])

        rank += 1

    df = pd.DataFrame(
        rows,
        columns=[
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    )

    df.to_csv(
        output_file,
        index=False
    )