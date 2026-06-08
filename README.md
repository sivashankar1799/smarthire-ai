# SmartHire AI

## Overview

SmartHire AI is an AI-powered candidate ranking system designed to help recruiters identify the best candidates for a role based on semantic understanding rather than keyword matching.

## Dataset Note

The original candidate dataset is not included in this repository because of file size limitations. Place the dataset in the data directory before running the project.

## Problem Statement

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching and often fail to identify strong candidates who possess relevant skills and experience but use different terminology.

This project addresses that challenge by combining semantic similarity, skill analysis, and behavioral signals to rank candidates intelligently.

## Project Structure

smarthire-ai/
│
├── data/
│   ├── job_description.docx
│   └── submission.csv
│
├── models/
│   ├── candidate_embeddings.npy
│   └── faiss_index.bin
│
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── jd_analyzer.py
│   ├── embeddings.py
│   ├── faiss_index.py
│   ├── ranking.py
│   ├── scoring.py
│   ├── skill_match.py
│   ├── startup_fit.py
│   ├── honeypot.py
│   └── exporter.py
│
├── README.md
└── requirements.txt

## Features

* AI candidate filtering
* Semantic job-description matching
* Skill-based scoring
* Behavioral signal analysis
* Candidate ranking engine
* Top-100 candidate recommendation
* CSV submission generation

## Architecture

Job Description
↓
AI Candidate Filter
↓
Sentence Transformer Embeddings
↓
FAISS Similarity Search
↓
Behavioral Scoring
↓
Final Candidate Ranking
↓
Top 100 Output

## Technologies Used

* Python
* Sentence Transformers
* FAISS
* NumPy
* Pandas
* python-docx

## Requirements

pip install -r requirements.txt


## Scoring Strategy

Final score combines:

* Semantic similarity
* Skill match score
* Startup experience
* Recruiter engagement signals
* Availability signals
* Honeypot detection penalty

## Results

The system successfully ranks AI-focused candidates such as:

* ML Engineers
* Data Scientists
* AI Research Engineers
* AI Specialists

while filtering out unrelated profiles.

## Usage

1. Place the job description in the data folder.
2. Run the application:

python src/main.py

3. The system generates:

data/submission.csv

containing the ranked candidate recommendations.

## Future Enhancements

* LLM-powered candidate reasoning
* Skill graph matching
* Real-time recruiter dashboard
* Multi-job ranking support

## Author

Siva Shankar
