

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
import matplotlib.pyplot as plt
import seaborn as sns

print("\n📊 Starting Univariate Analysis...\n")

# Select only important numeric columns
numeric_cols = ['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'parking']

# --------------------------------------------
# 1. Histograms (All in One Figure)
# --------------------------------------------
plt.figure(figsize=(15,10))

for i, col in enumerate(numeric_cols, 1):
    plt.subplot(3, 2, i)
    sns.histplot(df[col], kde=True, color='blue')
    plt.title(f"{col} Distribution")

plt.tight_layout()
plt.show()

# --------------------------------------------
# 2. Boxplots (All in One Figure)
# --------------------------------------------
plt.figure(figsize=(15,10))

for i, col in enumerate(numeric_cols, 1):
    plt.subplot(3, 2, i)
    sns.boxplot(x=df[col], color='orange')
    plt.title(f"{col} Boxplot")

plt.tight_layout()
plt.show()

# --------------------------------------------
# 3. Count Plot (Categorical)
# --------------------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x=df['furnishingstatus'])
plt.title("Furnishing Status Count")
plt.xticks(rotation=30)
plt.show()

print(Completed Successfully!")
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import chi2_contingency

print("\n📊 Starting Bivariate & Multivariate Analysis...\n")

# --------------------------------------------
# 1. Correlation Heatmap
# --------------------------------------------
plt.figure(figsize=(10,8))
corr_matrix = df.corr(numeric_only=True)

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")

plt.show()

# --------------------------------------------
# 2. Scatter Plot (Area vs Price)
# --------------------------------------------
plt.figure(figsize=(6,4))
sns.scatterplot(x='area', y='price', data=df)

plt.title("Area vs Price Relationship")

plt.show()

# --------------------------------------------
# 3. Boxplot (Price vs Furnishing Status)
# --------------------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(x='furnishingstatus', y='price', data=df)

plt.title("Price vs Furnishing Status")
plt.xticks(rotation=30)

plt.show()

# --------------------------------------------
# 4. Pairplot (Important Features)
# --------------------------------------------
important_cols = ['price', 'area', 'bedrooms', 'bathrooms', 'stories']

sns.pairplot(df[important_cols])

plt.show()

# --------------------------------------------
# 5. Chi-Square Test
# --------------------------------------------
print("\n🔹 Chi-Square Test: furnishingstatus vs airconditioning")

contingency_table = pd.crosstab(df['furnishingstatus'], df['airconditioning'])

chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f"Chi2 Value: {chi2:.2f}")
print(f"P-Value: {p:.4f}")

if p < 0.05:
    print("👉 Significant relationship between variables")
else:
    print("👉 No significant relationship")

# --------------------------------------------
# 6. Top Correlated Features with Price
# --------------------------------------------
print("\n🔹 Top Correlated Features with Price:")

top_corr = corr_matrix['price'].sort_values(ascending=False)
print(top_corr)

# --------------------------------------------
# END
# --------------------------------------------
print("Completed Successfully!")
