# ============================================
# DAY 5: STREAMLIT BASIC DASHBOARD
# ============================================

import streamlit as st
import pandas as pd

# Title
st.title("🏠 Housing Data Dashboard")

# Description
st.write("Basic EDA Dashboard using Streamlit")

# Load Dataset
df = pd.read_csv("Housing.csv")

# --------------------------------------------
# Show Data
# --------------------------------------------
st.subheader("📄 Dataset Preview")
st.dataframe(df)

# --------------------------------------------
# Show Shape
# --------------------------------------------
st.subheader("📊 Dataset Shape")
st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# --------------------------------------------
# Show Column Names
# --------------------------------------------
st.subheader("🧾 Column Names")
st.write(df.columns)

# --------------------------------------------
# Show Summary Statistics
# --------------------------------------------
st.subheader("📈 Statistical Summary")
st.write(df.describe())

# --------------------------------------------
# Missing Values
# --------------------------------------------
st.subheader("❗ Missing Values")
st.write(df.isnull().sum())

# --------------------------------------------
# Footer
# --------------------------------------------
st.write("Completed - Basic Dashboard Ready!")