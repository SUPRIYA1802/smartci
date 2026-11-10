import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load dataset
df = pd.read_csv("ml/builds.csv")

# Separate features and target
X = df.drop(columns=["failed"])
y = df["failed"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

print("\nMODEL ACCURACY:")
print(accuracy_score(y_test, predictions))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, predictions))

print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, predictions))

# Feature importance
print("\nFEATURE IMPORTANCE:")
for name, importance in zip(
    X.columns, model.feature_importances_
):
    print(name, round(importance, 4))

# Save model
joblib.dump(model, "ml/build_failure_model.joblib")

# Risky build
risky_build = pd.DataFrame([{
    "files_changed": 12,
    "lines_changed": 450,
    "hour": 22
}])

# Small well-tested build
small_build = pd.DataFrame([{
    "files_changed": 2,
    "lines_changed": 15,
    "hour": 10
}])

print("\nRISKY BUILD FAILURE PROBABILITY:")
print(model.predict_proba(risky_build)[0][1] * 100)

print("\nSMALL BUILD FAILURE PROBABILITY:")
print(model.predict_proba(small_build)[0][1] * 100)

print("\nMODEL SAVED SUCCESSFULLY!")
