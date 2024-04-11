import streamlit as st

st.write("""# Introducing Ross Fu!!""")
st.write("*Hello World!!!*")
st.write("*Welcome to my website!!!!*")


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title('Data Science Showcase')

# Sidebar
st.sidebar.title('Options')
data_load_state = st.sidebar.text('Loading data...')

# Load data
@st.cache
def load_data():
    # Load your dataset here
    # Example:
    # data = pd.read_csv('your_dataset.csv')
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100)
    })
    return data

data = load_data()
data_load_state.text('Loading data...done!')

# Show raw data
if st.sidebar.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(data)

# Data exploration
st.sidebar.subheader('Data Exploration')

# Scatter plot
if st.sidebar.checkbox('Show scatter plot'):
    st.subheader('Scatter Plot')
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='x', y='y')
    st.pyplot()

# Histogram
if st.sidebar.checkbox('Show histogram'):
    st.subheader('Histogram')
    plt.figure(figsize=(8, 6))
    sns.histplot(data['x'], bins=20, kde=True)
    st.pyplot()

# Correlation heatmap
if st.sidebar.checkbox('Show correlation heatmap'):
    st.subheader('Correlation Heatmap')
    corr = data.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    st.pyplot()

# Machine Learning
st.sidebar.title('Machine Learning')

# ML model training
if st.sidebar.checkbox('Train ML Model'):
    st.subheader('Train ML Model')
    # Your machine learning model training code goes here

# Conclusion
st.sidebar.title('Conclusion')
st.sidebar.write('Thanks for exploring!')

# About
st.sidebar.title('About')
st.sidebar.write('This app is a showcase of my data science abilities.')

