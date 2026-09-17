import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# ============================================================
# 1. LOAD DATASET
# ============================================================

DATASET_PATH = "fertilizer_recommendation_dataset.csv"

df = pd.read_csv(DATASET_PATH)

print("\nDataset loaded successfully!")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())


# ============================================================
# 2. REMOVE UNNECESSARY COLUMN
# ============================================================

# Remark is descriptive text and should not be used
# as a prediction feature.

if "Remark" in df.columns:
    df = df.drop(columns=["Remark"])


# ============================================================
# 3. DEFINE FEATURES AND TARGET
# ============================================================

TARGET = "Fertilizer"

X = df.drop(columns=[TARGET])
y = df[TARGET]

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget:", TARGET)

print("\nNumber of fertilizer classes:", y.nunique())

print("\nFertilizer distribution:")
print(y.value_counts())


# ============================================================
# 4. IDENTIFY NUMERIC AND CATEGORICAL FEATURES
# ============================================================

numeric_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()

print("\nNumeric features:")
print(numeric_features)

print("\nCategorical features:")
print(categorical_features)


# ============================================================
# 5. PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            StandardScaler(),
            numeric_features
        ),
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False
            ),
            categorical_features
        )
    ]
)


# ============================================================
# 6. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)


# ============================================================
# 7. DEFINE MODELS
# ============================================================

models = {

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1
    ),

    "KNN": KNeighborsClassifier(
        n_neighbors=5
    ),

    "SVM": SVC(
        kernel="rbf",
        random_state=42
    )
}


# ============================================================
# 8. TRAIN AND EVALUATE MODELS
# ============================================================

results = {}

trained_pipelines = {}

print("\n" + "=" * 60)
print("MODEL TRAINING")
print("=" * 60)

for name, model in models.items():

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    results[name] = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }

    trained_pipelines[name] = pipeline

    print(f"\n{name}")
    print("-" * 40)
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")


# ============================================================
# 9. DISPLAY COMPARISON
# ============================================================

results_df = pd.DataFrame(results).T

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(results_df)


# ============================================================
# 10. SELECT BEST MODEL
# ============================================================

best_model_name = results_df["f1"].idxmax()

best_pipeline = trained_pipelines[best_model_name]

print("\nBest Model:", best_model_name)
print("Best F1 Score:", results_df.loc[best_model_name, "f1"])


# ============================================================
# 11. SAVE BEST MODEL
# ============================================================

MODEL_PATH = "fertilizer_model.pkl"

joblib.dump(
    best_pipeline,
    MODEL_PATH
)

print("\nModel saved successfully!")
print("Saved as:", MODEL_PATH)

print("\nTraining completed successfully! 🎉")