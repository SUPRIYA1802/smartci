import os
import numpy as np
import pandas as pd

np.random.seed(42)

rows = 300

files_changed = np.random.randint(1, 30, rows)
lines_changed = np.random.randint(5, 1000, rows)
hour = np.random.randint(0, 24, rows)

risk = (
    0.025 * files_changed
    + 0.0015 * lines_changed
    + 0.035 * ((hour >= 22) | (hour <= 5))
)

probability = 1 / (1 + np.exp(-(risk - 1.5)))

failed = np.random.binomial(1, probability)

df = pd.DataFrame({
    "files_changed": files_changed,
    "lines_changed": lines_changed,
    "hour": hour,
    "failed": failed
})

os.makedirs("ml", exist_ok=True)
df.to_csv("ml/builds.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))
print("\nDataset preview:")
print(df.head())

print("\nBuild success/failure counts:")
print(df["failed"].value_counts())
