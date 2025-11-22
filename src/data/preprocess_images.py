"""
File: preprocess_images.py
Purpose: Prepare product images for encoding.

Description:
    - Loads image files from paths.
    - Applies resizing, cropping, and normalization.
    - Converts images into tensors suitable for ViT/CLIP encoders.
    - Optionally caches preprocessed images to disk.
"""
