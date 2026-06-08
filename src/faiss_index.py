import faiss
import numpy as np

def build_index(embeddings):

    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)

    index.add(
        embeddings.astype("float32")
    )

    return index


def search(
    index,
    query_embedding,
    top_k=1000
):

    scores, ids = index.search(
        query_embedding.reshape(1,-1).astype("float32"),
        top_k
    )

    return scores[0], ids[0]