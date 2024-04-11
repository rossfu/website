import streamlit as st

st.write("""# Introducing Ross Fu!!""")
st.write("*Hello World!!!*")
st.write("*Welcome to my website!!!!*")

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

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
    fig = px.scatter(data, x='x', y='y')
    st.plotly_chart(fig)

# Histogram
if st.sidebar.checkbox('Show histogram'):
    st.subheader('Histogram')
    fig = px.histogram(data, x='x', nbins=20)
    st.plotly_chart(fig)

# Correlation heatmap
if st.sidebar.checkbox('Show correlation heatmap'):
    st.subheader('Correlation Heatmap')
    corr = data.corr()
    fig = px.imshow(corr, color_continuous_scale='coolwarm')
    st.plotly_chart(fig)

# Machine Learning
st.sidebar.title('Machine Learning')

# ML model training
if st.sidebar.checkbox('Train ML Model'):
    st.subheader('T
