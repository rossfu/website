import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Set page config
st.set_page_config(
    page_title="Data Scientist Portfolio",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Title
st.title("Welcome to My Data Scientist Portfolio")

# Subheader
st.subheader("Explore data science visuals and machine learning demo")

# Introduction
st.write(
    "As a data scientist, I am passionate about leveraging data to drive "
    "insights and create impactful solutions. Dive into the visuals below "
    "and explore the machine learning demo to see predictive analytics in action."
)

# Spacer
st.write("")

# Section titles
st.markdown("## 1. Data Visualization")
st.markdown("## 2. Machine Learning Demo")

# Section 1: Data Visualization
st.markdown("### 1. Data Visualization")
st.write(
    "Visualizations are a powerful tool for communicating insights "
    "and trends in data. Explore the visuals below to gain new perspectives."
)

# Simple scatter plot
st.subheader("Simple Scatter Plot")
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
st.write(data)

# Section 2: Machine Learning Demo
st.markdown("### 2. Machine Learning Demo")
st.write(
    "Machine learning algorithms enable us to make predictions "
    "and decisions based on data. Explore the machine learning "
    "demo below to see predictive analytics in action."
)

# Iris dataset classification demo
st.subheader("Iris Dataset Classification Demo")
st.write(
    "In this demo, we use a Random Forest classifier to predict the species of iris flowers "
    "based on their sepal and petal dimensions."
)

# Load iris dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Train Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Make predictions
y_pred = rf_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

st.write(f"Accuracy: {accuracy:.2f}")

# Footer
st.write(
    "Thank you for exploring my data scientist portfolio! 📊💻"
    " Feel free to reach out for collaboration or project opportunities."
)
