"""
File: contrastive_loss.py
Purpose: Implement the InfoNCE contrastive loss for aligning context and item embeddings.

Description:
    - Computes positive and negative pair similarities in-batch.
    - Applies a temperature scaling parameter.
    - Encourages correct (context, item) pairs to be closer in embedding space.
"""
