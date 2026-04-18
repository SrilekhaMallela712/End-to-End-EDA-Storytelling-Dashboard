import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Housing Dashboard", layout="wide")

# Title
st.title("🏠 Housing Data Analysis Dashboard")

# Load Dataset
df = pd.read_csv("Housing.csv")

# --------------------------------------------
# Sidebar Navigation
# --------------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Filtered Data", "Visualizations"])

# --------------------------------------------
# Sidebar Filters
# --------------------------------------------
st.sidebar.header("🔍 Filters")

min_price = int(df['price'].min())
max_price = int(df['price'].max())

price_range = st.sidebar.slider(
    "Select Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

furnishing = st.sidebar.selectbox(
    "Furnishing Status",
    df['furnishingstatus'].unique()
)

# Apply Filters
filtered_df = df[
    (df['price'] >= price_range[0]) &
    (df['price'] <= price_range[1]) &
    (df['furnishingstatus'] == furnishing)
]

# --------------------------------------------
# PAGE 1: OVERVIEW
# --------------------------------------------
if page == "Overview":
    st.subheader("📄 Dataset Overview")
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Rows", df.shape[0])

    with col2:
        st.metric("Total Columns", df.shape[1])

    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    st.subheader("❗ Missing Values")
    st.write(df.isnull().sum())

# --------------------------------------------
# PAGE 2: FILTERED DATA
# --------------------------------------------
elif page == "Filtered Data":
    st.subheader("📄 Filtered Dataset")
    st.dataframe(filtered_df)

    csv = filtered_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="⬇️ Download Filtered Data",
        data=csv,
        file_name='filtered_housing_data.csv',
        mime='text/csv'
    )

# --------------------------------------------
# PAGE 3: VISUALIZATIONS
# --------------------------------------------
elif page == "Visualizations":

    st.subheader("📊 Select Visualization")

    graph = st.radio(
        "Choose Graph",
        ("Price Distribution", "Area vs Price", "Price vs Furnishing")
    )

    col1, col2 = st.columns([1, 3])

    with col2:
        if graph == "Price Distribution":
            st.subheader("📊 Price Distribution")
            fig, ax = plt.subplots()
            sns.histplot(filtered_df['price'], kde=True, ax=ax)
            st.pyplot(fig)

        elif graph == "Area vs Price":
            st.subheader("📈 Area vs Price")
            fig, ax = plt.subplots()
            sns.scatterplot(x='area', y='price', data=filtered_df, ax=ax)
            st.pyplot(fig)

        elif graph == "Price vs Furnishing":
            st.subheader("📦 Price vs Furnishing Status")
            fig, ax = plt.subplots()
            sns.boxplot(x='furnishingstatus', y='price', data=filtered_df, ax=ax)
            st.pyplot(fig)

# --------------------------------------------
# Footer
# --------------------------------------------
st.markdown("---")
st.write("📊 End-to-End EDA & Storytelling Dashboard using Streamlit")
