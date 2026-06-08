import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Smart Analytics Tool")

# Load Dataset
url = "https://raw.githubusercontent.com/AP-State-Skill-Development-Corporation/Datasets/master/Data%20Analysis/Advertising.csv"
df = pd.read_csv(url)

# Show Dataset
st.header("Dataset Preview")
st.dataframe(df.head())

# Dataset Shape
st.header("Dataset Information")
st.write("Rows and Columns:", df.shape)

# Summary Statistics
st.header("Summary Statistics")
st.write(df.describe())

# Correlation Heatmap
st.header("Correlation Analysis")

corr = df.corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Heatmap"
)

st.plotly_chart(fig)

# TV vs Sales
st.header("TV vs Sales Analysis")

fig2 = px.scatter(
    df,
    x="TV",
    y="sales",
    title="TV Advertisement vs Sales"
)

st.plotly_chart(fig2)

# Smart Insights
st.header("Smart Insights")

st.success("""
1. TV advertising has a strong positive relationship with sales.
2. Higher TV spending generally increases sales.
3. The dataset contains 200 observations.
4. Correlation analysis helps identify important features.
""")