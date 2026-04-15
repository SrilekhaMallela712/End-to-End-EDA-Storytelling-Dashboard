

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
# ============================================
# DAY 4: STATISTICAL TESTING
# ============================================

import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

print("\n📊 Starting Statistical Testing...\n")

# --------------------------------------------
# 1. Normality Test (Shapiro-Wilk Test)
# --------------------------------------------
print("\n🔹 Normality Test (Shapiro-Wilk):")

sample_data = df['price'].sample(100, random_state=42)

stat, p = stats.shapiro(sample_data)

print(f"Statistic: {stat:.4f}")
print(f"P-Value: {p:.4f}")

if p > 0.05:
    print("👉 Data is normally distributed")
else:
    print("👉 Data is NOT normally distributed")

# --------------------------------------------
# 2. Q-Q Plot
# --------------------------------------------
plt.figure(figsize=(6,4))
stats.probplot(df['price'], dist="norm", plot=plt)
plt.title("Q-Q Plot for Price")

plt.show(block=False)
plt.pause(3)
plt.close()

# --------------------------------------------
# 3. T-Test (Air Conditioning vs Price)
# --------------------------------------------
print("\n🔹 T-Test: Price vs Air Conditioning")

group1 = df[df['airconditioning'] == 1]['price']
group2 = df[df['airconditioning'] == 0]['price']

t_stat, p_val = stats.ttest_ind(group1, group2)

print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val:.4f}")

if p_val < 0.05:
    print("👉 Significant difference between groups")
else:
    print("👉 No significant difference")

# --------------------------------------------
# 4. ANOVA Test (Furnishing Status vs Price)
# --------------------------------------------
print("\n🔹 ANOVA Test: Price vs Furnishing Status")

groups = [group['price'].values for name, group in df.groupby('furnishingstatus')]

f_stat, p_val = stats.f_oneway(*groups)

print(f"F-Statistic: {f_stat:.4f}")
print(f"P-Value: {p_val:.4f}")

if p_val < 0.05:
    print("👉 At least one group is significantly different")
else:
    print("👉 No significant difference among groups")

# --------------------------------------------
# 5. Mann-Whitney U Test (Non-Parametric)
# --------------------------------------------
print("\n🔹 Mann-Whitney U Test: Price vs Guestroom")

group1 = df[df['guestroom'] == 1]['price']
group2 = df[df['guestroom'] == 0]['price']

u_stat, p_val = stats.mannwhitneyu(group1, group2)

print(f"U-Statistic: {u_stat:.4f}")
print(f"P-Value: {p_val:.4f}")

if p_val < 0.05:
    print("👉 Significant difference between groups")
else:
    print("👉 No significant difference")

# --------------------------------------------
# FINAL MESSAGE
# --------------------------------------------
print("Completed Successfully!")
