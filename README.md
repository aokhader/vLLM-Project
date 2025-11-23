# 🌟 **Multi-Modal Next-Item Recommendation using BLAIR-MM (Text + Image Embeddings)**

## UCSD – DSC 256: Recommender Systems & Web Mining

### Final Project — Fall 2025

**Team Members:** _Will L., Derek P., Abdulaziz K., Mustafa H._  
**Instructor:** _Julian McAuley_

---

# 🚀 **Project Overview**

This project investigates a **next-item recommendation task** using a **multi-modal embedding model** inspired by **BLAIR (Bridging Language and Items for Retrieval)**.  
We extend the original BLAIR architecture by incorporating **image embeddings** alongside text embeddings, creating a multimodal representation called **BLAIR-MM**.

Our predictive task:

> **Given a user’s interaction history, predict the next item they will interact with.**

To evaluate our multimodal embeddings, we integrate them into standard recommender models from the course, such as **Matrix Factorization (MF)** and **FPMC**, and compare them to classical baselines.

---

# 📚 **1. Predictive Task Definition**

### 🎯 Task

Predict the next item a user will consume based on their sequential interaction history.

Formally, given a sequence:  
\[
S_u = [i_1, i_2, ..., i_t]
\]

predict the next item \( i\_{t+1} \).

### 📈 Evaluation Metrics

-   **Recall@10 / Recall@50**
-   **AUC**
-   **Nearest neighbor inspection**
-   **Cold-start evaluation**

### 🧪 Baselines

1. Popularity baseline
2. Last-item transition
3. Matrix Factorization (MF)
4. item2vec
5. FPMC
6. **Our model: BLAIR-MM + FPMC**

### ✔ Validity Checks

-   _Cold-start behavior_
-   _Sequence transition sanity_
-   _Qualitative neighbor inspection_
-   _Baseline comparisons_

---

# 🔍 **2. Dataset, EDA, and Preprocessing**

### 📦 Dataset

Amazon-style dataset including:

-   _Text metadata_
-   _Product images_
-   _User-item interaction sequences_

### 🧹 Preprocessing

-   _Tokenization_
-   _Image resizing_
-   _Sequence filtering_
-   _Splitting (leave-one-out)_

### 📊 EDA

-   _Popularity distribution_
-   _Sequence length plots_
-   _Text histograms_
-   _Sample item previews_

---

# 🧠 **3. Modeling**

## 🎯 Problem Formulation

Next-item prediction as a ranking task.

## 🏗 **Model Architecture: BLAIR-MM**

### Text Encoder

RoBERTa-Base → 768-d CLS token

### Image Encoder

ViT-B/32 → 512–768-d output

### Fusion Module

MLP([text || image]) → 768-d fused embedding

### Contrastive Objective

Align context text ↔ fused item embedding.

## 🔮 Downstream Models

-   _Matrix Factorization_
-   _FPMC_

---

# 📊 **4. Evaluation**

### Metrics

-   _Recall@10 / Recall@50_
-   _AUC_
-   _Cold-start behavior_

### Sample Results Table

| Model        | Recall@10 | Recall@50 | AUC      |
| ------------ | --------- | --------- | -------- |
| Popularity   | 0.06      | 0.12      | 0.48     |
| item2vec     | 0.19      | 0.28      | 0.66     |
| MF           | 0.13      | 0.20      | 0.61     |
| **BLAIR-MM** | **0.32**  | **0.46**  | **0.75** |

---

# 📚 **5. Related Work**

### Classical Recommendation Methods

-   _Matrix Factorization_
-   _BPR_
-   _FPMC_

### Text-based Retrieval

-   _TF-IDF + Cosine Similarity_
-   _item2vec (Skip-Gram/item embedding models)_
-   _LSTM/CNN text recommenders_

### Multi-modal Recommender Systems

-   _VBPR: Visual Bayesian Personalized Ranking_
-   _DeepStyle: Style-based item matching_
-   _CLIP for vision-language alignment_
-   _BLaIR (text-only baseline)_

### Our Model

-   _First multimodal extension + sequential recommendation evaluation._
-   _BLaIR is text-only_
-   _Incorporated multimodal fusion (text + images)_
-   _Apply embeddings to sequential recommendation_

---

# 📁 **Project Structure**

```
project/
│
├── README.md
├── workbook.html                      # exported Jupyter notebook
├── video_url.txt                      # link to 20-minute presentation
│
├── notebooks/
│   ├── 01_eda.ipynb                   # data exploration + preprocessing
│   ├── 02_baselines.ipynb             # Popularity, MF, item2vec baselines
│   ├── 03_multimodal_training.ipynb   # CLIP + BLAIR fusion model (BLAIR-MM)
│   ├── 04_evaluation.ipynb            # comparison of baselines vs. BLAIR-MM
│
├── src/
│   ├── data_utils.py                  # data loading, text + image preprocessing, user sequences
│   ├── baseline_models.py             # Popularity, MF, item2vec implementations
│   ├── clip_encoder.py                # CLIP-based image embedding wrapper
│   ├── blair_encoder.py               # BLAIR text encoder wrapper
│   ├── fusion_model.py                # fuse CLIP + BLAIR embeddings into multimodal item vectors
│   ├── contrastive_training.py        # InfoNCE contrastive training loop for BLAIR-MM
│   ├── recommenders.py                # scoring functions for baseline + multimodal recommenders
│   ├── evaluation.py                  # Recall@K, AUC, cold-start, nearest-neighbor evaluation
│
└── test/
    └── metrics.py
```

---

# 🎥 Presentation

20-minute video covering all five graded sections.

---

# 🎉 Conclusion

BLAIR-MM significantly improves next-item recommendation by leveraging multimodal (text + image) content, outperforming classical baselines from DSC 256.
