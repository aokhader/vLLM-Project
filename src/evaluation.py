"""
File: evaluation.py
Purpose:
    Compute evaluation metrics and compare all models on next-item prediction.

This file should:
    • Implement Recall@K and AUC metrics.
    • Provide evaluate_model(model, test_data) -> metric_dict
    • Provide evaluate_all(models, test_data) -> comparison_table
    • Support cold-start evaluation and nearest-neighbor inspection.

Used by:
    • Notebook 04 (Final Evaluation + Comparison Table)
"""
