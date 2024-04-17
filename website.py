import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Set page config
st.set_page_config(
    page_title="Eric Ross Fu's Data Science Website",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
)




# Title
st.title("Hello, welcome to Eric Ross Fu's website!")


# Spacer
st.write("")

# Create two columns
col1,col2 = st.columns(2)

with col1:
    image_url = "https://github.com/rossfu/website/blob/main/headshot.jpg?raw=true"
    st.image(image_url, width = 300)

with col2:
    st.subheader("Data Scientist @ Avance Biosciences")
    st.write("https://www.linkedin.com/in/eric-ross-fu")
    st.write("https://github.com/rossfu")
    st.write("ericrossfu@yahoo.com")
    st.write("713-540-4528")

st.write("")
st.write("")
st.write("")
# Play background music
audio_file = open('Future, Metro Boomin - Slimed In (Official Audio).mp3', 'rb')
st.audio(audio_file, format='audio/mp3', start_time=0)
st.write("Here's a cool graph")


# Generate sample data
np.random.seed(0)
n_points = 100
x = np.random.rand(n_points)
y = np.random.rand(n_points)
z = np.random.rand(n_points)
color = np.random.rand(n_points)
size = np.random.rand(n_points) * 30

# Create 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=size,
        color=color,
        opacity=0.8,
        colorscale='Viridis'
    )
)])

# Customize layout
fig.update_layout(
    scene=dict(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        zaxis_title='Z-axis'
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)

# Display plot
st.plotly_chart(fig)
