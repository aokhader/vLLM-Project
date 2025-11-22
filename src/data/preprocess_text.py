"""
File: preprocess_text.py
Purpose: Clean and tokenize item text metadata.

Description:
    - Applies text normalization (lowercasing, filtering, etc.).
    - Uses a Transformer tokenizer (e.g., RoBERTa) to convert text into token IDs.
    - Truncates text to a fixed max length and returns model-ready inputs.
"""
