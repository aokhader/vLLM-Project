"""
File: clip_encoder.py
Purpose:
    Wrap the CLIP image encoder and produce image embeddings for each item.

This file should:
    • Load a pretrained CLIP image encoder (ViT backbone).
    • Preprocess images into CLIP’s expected format.
    • Provide a function encode_images(image_paths) -> torch.Tensor
    • Allow batch encoding and optional caching for speed.

Used by:
    • Notebook 03 (Multimodal Training)
"""
