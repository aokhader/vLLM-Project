"""
File: text_encoder.py
Purpose: Wrap a Transformer text model to encode item text metadata.

Description:
    - Uses a pretrained RoBERTa/BERT model to generate text embeddings.
    - Extracts the CLS token as the fixed-length representation.
    - Normalizes embeddings for use in contrastive training.
"""
