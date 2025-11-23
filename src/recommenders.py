"""
File: recommenders.py
Purpose:
    Provide scorers for next-item prediction using baseline and multimodal models.

This file should include:
    • MFScorer:
         - Uses MF user vectors + item vectors to rank items.
    • Item2VecScorer:
         - Uses item2vec embeddings for similarity-based recommendation.
    • MultimodalScorer:
         - Uses fused CLIP+BLAIR embeddings for ranking.
         - Combines multimodal item embeddings with simple user embeddings
           (e.g., MF-style learned user vectors).

Each scorer must expose:
    • score(user_id) -> ranked list of items

Used by:
    • Notebook 04 (Evaluation)
"""
