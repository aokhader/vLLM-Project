"""
File: baseline_models.py
Purpose:
    Implement the classical DSC 256 baseline models for comparison.

This file should include:
    • Popularity baseline:
        - Ranks items by global frequency.
    • Matrix Factorization baseline:
        - Learns user/item latent factors using implicit feedback.
    • item2vec baseline:
        - Trains Skip-Gram item embeddings from user sequences.

Each baseline should expose:
    • fit(...)       — trains the baseline model.
    • predict(user)  — returns ranked items for the user.

Used by:
    • Notebook 02 (Baselines)
    • Notebook 04 (Final Evaluation)
"""
