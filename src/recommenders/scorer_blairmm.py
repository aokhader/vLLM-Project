"""
File: scorer_blairemm.py
Purpose: Use BLAIR-MM multimodal embeddings for next-item recommendation.

Description:
    - Takes fused (text + image) item embeddings.
    - Combines them with user embeddings (MF or FPMC-style) to score items.
    - Provides the main model compared against classical baselines.
"""
