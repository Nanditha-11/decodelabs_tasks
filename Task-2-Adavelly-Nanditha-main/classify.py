
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    print("===================================================")
    print("  Classification   ")
    print("===================================================\n")

    # 1. Load Dataset
    print("[1] Loading Iris Benchmark Dataset...")
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names
    print(f"    - Total samples: {X.shape[0]}")
    print(f"    - Features: {feature_names}")
    print(f"    - Target species: {list(target_names)}\n")

    # 2. Split data into training and testing sets
    print("[2] Splitting data into Training (80%) and Testing (20%) sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=True, random_state=42
    )
    print(f"    - Training samples: {len(X_train)}")
    print(f"    - Testing samples: {len(X_test)}\n")

    # 3. Apply Feature Scaling
    print("[3] Standardizing features using StandardScaler...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("    - Feature mean centered to 0, variance scaled to 1.\n")

    # 4. Train and Evaluate K-Nearest Neighbors (KNN)
    print("[4] Training K-Nearest Neighbors Classifier (K=5)...")
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train_scaled, y_train)
    knn_preds = knn.predict(X_test_scaled)
    knn_acc = accuracy_score(y_test, knn_preds)
    
    print("\n--- KNN Classification Report ---")
    print(f"Accuracy: {knn_acc * 100:.1f}%")
    print(classification_report(y_test, knn_preds, target_names=target_names))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, knn_preds))
    print("---------------------------------\n")

    # 5. Train and Evaluate Decision Tree Classifier
    print("[5] Training Decision Tree Classifier...")
    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train_scaled, y_train)
    dt_preds = dt.predict(X_test_scaled)
    dt_acc = accuracy_score(y_test, dt_preds)

    print("--- Decision Tree Classification Report ---")
    print(f"Accuracy: {dt_acc * 100:.1f}%")
    print(classification_report(y_test, dt_preds, target_names=target_names))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, dt_preds))
    print("-------------------------------------------\n")

    # 6. Direct Inference on a New Flower Measurement
    new_flower = [[5.1, 3.5, 1.4, 0.2]]
    print(f"[6] Performing Direct Classification on new flower measurement: {new_flower}")
    
    # Scale new measurement before passing to models
    new_flower_scaled = scaler.transform(new_flower)
    
    # KNN Prediction
    knn_pred_class = knn.predict(new_flower_scaled)[0]
    knn_prob = knn.predict_proba(new_flower_scaled)[0][knn_pred_class]
    
    # Decision Tree Prediction
    dt_pred_class = dt.predict(new_flower_scaled)[0]
    dt_prob = dt.predict_proba(new_flower_scaled)[0][dt_pred_class]

    print(f"\n    * KNN Prediction:           Iris {target_names[knn_pred_class]} ({knn_prob * 100:.1f}% confidence)")
    print(f"    * Decision Tree Prediction:  Iris {target_names[dt_pred_class]} ({dt_prob * 100:.1f}% confidence)\n")

if __name__ == "__main__":
    main()
