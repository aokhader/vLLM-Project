"""
File: blair_encoder.py
Purpose:
    Wrap the BLAIR text encoder to compute embeddings for item text and context text.

This file should:
    • Load a pretrained BLAIR text encoder (e.g., RoBERTa backbone).
    • Tokenize item titles/descriptions.
    • Provide encode_text(text_list) -> torch.Tensor
    • Return normalized embeddings suitable for contrastive learning.

Used by:
    • Notebook 03 (Multimodal Training)
    • Notebook 04 (Scoring with multimodal embeddings)
"""
