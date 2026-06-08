# SmartHire AI

## Overview

SmartHire AI is an AI-powered candidate ranking system designed to help recruiters identify the best candidates for a role based on semantic understanding rather than keyword matching.

## Problem Statement

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching and often fail to identify strong candidates who possess relevant skills and experience but use different terminology.

This project addresses that challenge by combining semantic similarity, skill analysis, and behavioral signals to rank candidates intelligently.

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

## Future Enhancements

* LLM-powered candidate reasoning
* Skill graph matching
* Real-time recruiter dashboard
* Multi-job ranking support

## Author

Siva Shankar
