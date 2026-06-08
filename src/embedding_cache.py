# src/embedding_cache.py

import os
import numpy as np

def save_embeddings(path, embeddings):

    np.save(
        path,
        embeddings
    )

def load_embeddings(path):

    return np.load(path)