"""
File: scorer_item2vec.py
Purpose: Generate next-item predictions using item2vec embeddings.

Description:
    - Computes similarity between last-item embedding and all other items.
    - Ranks candidate items by cosine similarity.
    - Matches the evaluation framework used in the baseline comparison.
"""
