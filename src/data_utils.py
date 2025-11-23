"""
File: data_utils.py
Purpose:
    Utilities for loading, cleaning, and preparing the dataset used in the project.

This file should:
    • Load item metadata (titles, descriptions) and image paths.
    • Load user-item interaction logs.
    • Preprocess text (basic cleaning + tokenization if needed).
    • Preprocess images into tensors suitable for CLIP encoders.
    • Build chronological user sequences for next-item prediction.
    • Generate train/validation/test splits using leave-one-out.

Used by:
    • Notebook 01 (EDA)
    • Notebooks 02–04 (for loading sequences and item data)
"""
