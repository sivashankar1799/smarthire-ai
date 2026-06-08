import json
from docx import Document

def load_job_description(path):
    doc = Document(path)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)

def load_candidates(path):

    candidates = []

    with open(path,"r",encoding="utf-8") as f:

        for line in f:
            candidates.append(json.loads(line))

    return candidates