import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Data Scientist Portfolio",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Title
st.title("Welcome to My Data Scientist Portfolio")

# Header image
st.image("https://source.unsplash.com/random/800x300", use_column_width=True)

# Subheader
st.subheader("Explore stunning visualizations and machine learning demos")

# Introduction
st.write(
    "As a data scientist, I am passionate about leveraging data to drive "
    "insights and create impactful solutions. Dive into the visualizations "
    "below to experience the power of data storytelling, and explore the "
    "machine learning demos to see predictive analytics in action."
)

# Spacer
st.write("")

# Section titles
st.markdown("## 1. Stunning Visualizations")
st.markdown("## 2. Machine Learning Demos")

# Section 1: Stunning Visualizations
st.markdown("### 1. Stunning Visualizations")
st.write(
    "Visualizations are a powerful tool for communicating insights "
    "and trends in data. Explore these stunning visualizations to "
    "gain new perspectives and uncover hidden patterns."
)

# Scatter plot
st.subheader("Scatter Plot")
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
fig = px.scatter(data, x='x', y='y')
st.plotly_chart(fig)

# Spacer
st.write("")

# Section 2: Machine Learning Demos
st.markdown("### 2. Machine Learning Demos")
st.write(
    "Machine learning algorithms enable us to make predictions "
    "and decisions based on data. Explore these machine learning "
    "demos to see predictive analytics in action."
)

# Iris dataset classification demo
st.subheader("Iris Dataset Classification Demo")
st.write(
    "In this demo, we use a Random Forest classifier to predict the species of iris flowers "
    "based on their sepal and petal dimensions."
)

# Footer
st.write(
    "Thank you for exploring my data scientist portfolio! 📊💻"
    " Feel free to reach out for collaboration or project opportunities."
)
