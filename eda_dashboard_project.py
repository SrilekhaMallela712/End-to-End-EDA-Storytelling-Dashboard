# ============================================
# DAY 1: DATA INGESTION & DATA QUALITY AUDIT
# ============================================

# Import Libraries
import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("Housing.csv")

print("✅ Dataset Loaded Successfully!\n")

# --------------------------------------------
# 1. Basic Information
# --------------------------------------------
print("🔹 Dataset Shape (Rows, Columns):")
print(df.shape)

print("\n🔹 Column Names:")
print(df.columns)

print("\n🔹 Dataset Info:")
df.info()

print("\n🔹 Statistical Summary:")
print(df.describe())

# --------------------------------------------
# 2. Missing Values Analysis
# --------------------------------------------
print("\n🔹 Missing Values Count:")
print(df.isnull().sum())

print("\n🔹 Missing Values Percentage:")
print((df.isnull().sum() / len(df)) * 100)

# --------------------------------------------
# 3. Duplicate Check
# --------------------------------------------
print("\n🔹 Duplicate Rows:")
print(df.duplicated().sum())

# --------------------------------------------
# 4. Unique Values in Each Column
# --------------------------------------------
print("\n🔹 Unique Values Count:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()}")

# --------------------------------------------
# 5. Convert Yes/No to 1/0
# --------------------------------------------
binary_cols = [
    'mainroad',
    'guestroom',
    'basement',
    'hotwaterheating',
    'airconditioning',
    'prefarea'
]

for col in binary_cols:
    df[col] = df[col].map({'yes': 1, 'no': 0})

print("\n✅ Converted categorical (yes/no) to numeric")

# --------------------------------------------
# 6. Outlier Detection (IQR Method)
# --------------------------------------------
print("\n🔹 Outlier Detection:")

numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    outliers = df[
        (df[col] < Q1 - 1.5 * IQR) |
        (df[col] > Q3 + 1.5 * IQR)
    ]

    print(f"{col}: {len(outliers)} outliers")

# --------------------------------------------
# 7. Save Cleaned Dataset
# --------------------------------------------
df.to_csv("cleaned_housing.csv", index=False)

print("Completed Successfully!")