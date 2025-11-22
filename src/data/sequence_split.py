"""
File: sequence_split.py
Purpose: Build user interaction sequences and generate train/valid/test splits.

Description:
    - Converts raw user-item interactions into ordered sequences.
    - Applies leave-one-out splitting for next-item prediction tasks.
    - Prevents data leakage by ensuring chronological order.
"""
