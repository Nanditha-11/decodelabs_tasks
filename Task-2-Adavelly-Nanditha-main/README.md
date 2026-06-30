# DecodeLabs AI Data Classifier — Project 2
**Project Name:** Data Classification Using AI (Supervised Learning Pipeline)  

---

## 📌 Project Overview
This project is part of the **DecodeLabs Industrial Training program (Project 2)**. 

It implements a supervised learning data classification pipeline utilizing scikit-learn. The application is consolidated into a single script that runs entirely within the terminal, executing feature scaling, train-test splitting, dual-classifier training (KNN and Decision Tree), diagnostic evaluation, and direct classification inference.

---

## ⚙️ Features
1. **Feature Scaling (The Gatekeeper Rule)**: Employs `StandardScaler` to normalize dimensions to mean = 0 and variance = 1, ensuring distance calculations are unbiased.
2. **Structural Integrity Split**: Shuffles and partitions the dataset into an 80% Training set (for learning patterns) and a 20% Testing set (for validation).
3. **Dual Model Evaluation**: Trains, tests, and validates both **K-Nearest Neighbors (KNN)** and **Decision Tree** classifiers side-by-side.
4. **Diagnostic Metrics**: Generates confusion matrices and classification reports containing Accuracy, Precision, Recall, and F1-Scores.
5. **Direct Inference**: Classifies novel flower inputs in real-time and computes prediction confidences.

---

## 📁 File Structure
```text
C:\Users\nandi\Documents\AI Project 2\
└── classify.py   # Direct Python AI Data Classifier
```

---

## 🚀 How to Run the Classifier

Since this classifier requires external machine learning packages, make sure you have `numpy`, `pandas`, and `scikit-learn` installed.

1. Open your terminal or Command Prompt in the project directory.
2. Run the classifier using Python:
   ```bash
   python classify.py
   ```

---

## 📊 Pipeline Phase Details

The steps executed sequentially by the pipeline are detailed below:

| Pipeline Phase | Step & Implementation | Detail / Metrics |
|---|---|---|
| **1. Input Data** | Load Iris Benchmark Dataset | Loads 150 balanced samples across 3 species (setosa, versicolor, virginica). |
| **2. Preprocessing** | StandardScaler Feature Scaling | Standardizes all 4 features (sepal/petal dimensions) to zero mean and unit variance. |
| **3. Processing** | Train-Test Split | Splitting data: 120 samples for training, 30 samples for testing. |
| **4. KNN Classifier** | KNeighborsClassifier (K=5) | Querying neighborhood votes for classification (Achieves 100% Accuracy). |
| **5. Decision Tree** | DecisionTreeClassifier | Constructing logical binary splits to categorize points (Achieves 100% Accuracy). |
| **6. Output Diagnostic** | Confusion Matrix | Generates 3x3 counts representing correct and incorrect classifications. |
| **7. Metric Evaluation** | Classification Report | Computes class-wise Precision, Recall, and F1-Score (Harmonic Mean). |
| **8. Inference** | Custom Flower Prediction | Inputting [[5.1, 3.5, 1.4, 0.2]] predicts Iris Setosa (100% confidence). |
