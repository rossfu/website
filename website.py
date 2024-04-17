import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Set page config
st.set_page_config(
    page_title="Eric Ross Fu's Data Science Website",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Title
st.title("Hello, welcome to Eric Ross Fu's website!")


# Play background music
audio_file = open('Future, Metro Boomin - Slimed In (Official Audio).mp3', 'rb')
st.audio(audio_file, format='audio/mp3', start_time=0)


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




# Email me function

def send_email(name, email, job_description):
    # Email configurations
    sender_email = "ericrossfu@yahoo.com"  # Replace with your Yahoo email
    receiver_email = "ericrossfu@yahoo.com"  # Replace with your Yahoo email

    person_who_inquired_email = email
    
    app_specific_password = "qshbgubfeexbmekh"  # Replace with your Yahoo app-specific password
    smtp_server = "smtp.mail.yahoo.com"  # Yahoo SMTP server
    smtp_port = 587  # Use 587 for TLS/STARTTLS or 465 for SSL
    
    # Email content
    subject = "Streamlit Contact Request!"
    message = f"Name: {name}\nEmail: {email}\nJob Opportunity Description:\n{job_description}"
    
    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS
        server.login(sender_email, app_specific_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


    # Lets send a reply
    subject2 = "Thanks for emailing Eric Ross Fu!"
    message2 = f"Hey {name},\n\nI appreciate hearing from you. \nThis is an automated reply. \nThe best way to reach me is 7135404528.\n\n\nBest,\nEric Ross Fu\nData Scientist at Avance Biosciences"
    
    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = person_who_inquired_email
    msg['Subject'] = subject2
    msg.attach(MIMEText(message2, 'plain'))
    
    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS
        server.login(sender_email, app_specific_password)
        server.sendmail(sender_email, person_who_inquired_email, msg.as_string())





# Contact me Function
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.title('Contact Me')
contact_button = st.button('Contact Me')

if 'name' not in st.session_state:
    st.session_state.name = ''
if 'email' not in st.session_state:
    st.session_state.email = ''
if 'job_description' not in st.session_state:
    st.session_state.job_description = ''

if contact_button:
    st.write('Please provide the following details:')
    
    # Get user input for name
    st.session_state.name = st.text_input('Name:', st.session_state.name)

    # Get user input for email
    st.session_state.email = st.text_input('Email Address:', st.session_state.email)

    # Get user input for job opportunity description
    st.session_state.job_description = st.text_area('Description of Job Opportunity:', st.session_state.job_description)

    if st.button('Send'):
        # Send email with user details
        send_email(st.session_state.name, st.session_state.email, st.session_state.job_description)
        
        # Display confirmation
        st.write('Thank you for reaching out! Your inquiry has been sent.')

