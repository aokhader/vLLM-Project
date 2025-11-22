"""
File: image_encoder.py
Purpose: Encode item images using a vision backbone (ViT or CLIP).

Description:
    - Loads and applies a pretrained transformer-based image encoder.
    - Produces fixed-length image embeddings for downstream fusion.
    - Supports normalization and optional embedding caching.
"""
