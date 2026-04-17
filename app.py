import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("🏠 Housing Data Dashboard")

# Load Dataset
df = pd.read_csv("Housing.csv")

# --------------------------------------------
# Sidebar Filters
# --------------------------------------------
st.sidebar.header("🔍 Filter Data")

min_price = int(df['price'].min())
max_price = int(df['price'].max())

price_range = st.sidebar.slider(
    "Select Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

furnishing = st.sidebar.selectbox(
    "Select Furnishing Status",
    df['furnishingstatus'].unique()
)

# Apply Filters
filtered_df = df[
    (df['price'] >= price_range[0]) &
    (df['price'] <= price_range[1]) &
    (df['furnishingstatus'] == furnishing)
]

# --------------------------------------------
# Show Filtered Data
# --------------------------------------------
st.subheader("📄 Filtered Data")
st.dataframe(filtered_df)

# --------------------------------------------
# Layout (Left: Options, Right: Graph)
# --------------------------------------------
col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("📊 Select Graph")

    graph_option = st.radio(
        "Choose:",
        ("Price Distribution", "Area vs Price", "Price vs Furnishing")
    )

# --------------------------------------------
# Show Graph Based on Selection
# --------------------------------------------
with col2:
    if graph_option == "Price Distribution":
        st.subheader("📊 Price Distribution")
        fig, ax = plt.subplots()
        sns.histplot(filtered_df['price'], kde=True, ax=ax)
        st.pyplot(fig)

    elif graph_option == "Area vs Price":
        st.subheader("📈 Area vs Price")
        fig, ax = plt.subplots()
        sns.scatterplot(x='area', y='price', data=filtered_df, ax=ax)
        st.pyplot(fig)

    elif graph_option == "Price vs Furnishing":
        st.subheader("📦 Price vs Furnishing Status")
        fig, ax = plt.subplots()
        sns.boxplot(x='furnishingstatus', y='price', data=filtered_df, ax=ax)
        st.pyplot(fig)

# --------------------------------------------
# Footer
# --------------------------------------------
st.write("Completed - Interactive Dashboard Ready!")
