import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from xgboost import XGBClassifier

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("crop_recommendation.csv")


# -----------------------------
# 2. Separate features and target
# -----------------------------
X = df.drop("label", axis=1)
y = df["label"]


# -----------------------------
# 3. Check dataset
# -----------------------------
print("X shape:", X.shape)
print("y shape:", y.shape)
print("Duplicate rows:", df.duplicated().sum())


# -----------------------------
# 4. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)




# -----------------------------
# 5. Create Decision Tree
# -----------------------------
model = DecisionTreeClassifier(random_state=42)


# -----------------------------
# 6. Train model
# -----------------------------
model.fit(X_train, y_train)


# -----------------------------
# 7. Make predictions
# -----------------------------
y_pred = model.predict(X_test)


# -----------------------------
# 8. Evaluate
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nDecision Tree Accuracy:", accuracy)




# -----------------------------
# Random Forest
# -----------------------------
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_pred)

print("Random Forest Accuracy:", rf_accuracy)



# -----------------------------
# Scale data for KNN
# -----------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)




# -----------------------------
# KNN
# -----------------------------
knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train_scaled, y_train)

knn_pred = knn_model.predict(X_test_scaled)

knn_accuracy = accuracy_score(y_test, knn_pred)

print("KNN Accuracy:", knn_accuracy)



# -----------------------------
# SVM
# -----------------------------
svm_model = SVC(kernel="rbf")

svm_model.fit(X_train_scaled, y_train)

svm_pred = svm_model.predict(X_test_scaled)

svm_accuracy = accuracy_score(y_test, svm_pred)

print("SVM Accuracy:", svm_accuracy)



#  this onward is XGboost

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)


# XGBoost
xgb_model = XGBClassifier(
    n_estimators=100,
    random_state=42,
    eval_metric="mlogloss"
)

xgb_model.fit(X_train, y_train_encoded)

xgb_pred_encoded = xgb_model.predict(X_test)

xgb_accuracy = accuracy_score(y_test_encoded, xgb_pred_encoded)

print("XGBoost Accuracy:", xgb_accuracy)

# Model predictions


 # Evaluate all models

models = {
    "Decision Tree": model,
    "Random Forest": rf_model,
    "KNN": knn_model,
    "SVM": svm_model
}

print("\n========== MODEL EVALUATION ==========")

for model_name, model in models.items():

    # KNN and SVM need scaled data
    if model_name in ["KNN", "SVM"]:
        predictions_value = model.predict(X_test_scaled)
    else:
        predictions_value = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions_value)

    precision = precision_score(
        y_test,
        predictions_value,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        predictions_value,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        predictions_value,
        average="weighted"
    )

    print(f"\n{model_name}")
    print("Accuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)


# XGBoost evaluation
xgb_predictions = label_encoder.inverse_transform(xgb_pred_encoded)

xgb_accuracy = accuracy_score(y_test, xgb_predictions)

xgb_precision = precision_score(
    y_test,
    xgb_predictions,
    average="weighted"
)

xgb_recall = recall_score(
    y_test,
    xgb_predictions,
    average="weighted"
)

xgb_f1 = f1_score(
    y_test,
    xgb_predictions,
    average="weighted"
)

print("\nXGBoost")
print("Accuracy :", xgb_accuracy)
print("Precision:", xgb_precision)
print("Recall   :", xgb_recall)
print("F1 Score :", xgb_f1)


# -----------------------------
# Random Forest Confusion Matrix
# -----------------------------

cm = confusion_matrix(y_test, rf_pred)

plt.figure(figsize=(14, 12))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=sorted(y.unique()),
    yticklabels=sorted(y.unique())
)

plt.xlabel("Predicted Crop")
plt.ylabel("Actual Crop")
plt.title("Random Forest Confusion Matrix")

plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()

# -----------------------------
# Save final Crop Recommendation Model
# -----------------------------

joblib.dump(rf_model, "crop_model.pkl")

print("\nRandom Forest model saved as crop_model.pkl")