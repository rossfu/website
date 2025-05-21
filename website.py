import streamlit as st
import pandas as pd
import numpy as np

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Set page config
st.set_page_config(
    page_title="Eric Ross Fu's Data Science Website",
    page_icon="https://github.com/rossfu/website/raw/main/favicon-16x16.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Title
st.title("Hello, welcome to Eric Fu's website!")


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
st.write("")



# AI #########################################################################################################################
import os
import requests
from llama_cpp import Llama

# --- Model info ---
MODEL_URL = "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q2_K.gguf"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "tinyllama.Q2_K.gguf")

# --- Download GGUF model if not already downloaded ---
def download_model():
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
    if not os.path.exists(MODEL_PATH):
        with st.spinner("⏳ Downloading model..."):
            response = requests.get(MODEL_URL, stream=True)
            with open(MODEL_PATH, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        st.success("✅ Model downloaded!")

# --- Load model only when user clicks a button ---
def load_model():
    if not os.path.exists(MODEL_PATH):
        download_model()
    with st.spinner("🧠 Loading model..."):
        llm = Llama(model_path=MODEL_PATH, n_threads=4)
        st.session_state.llm = llm
        st.success("✅ Model loaded and ready!")

# --- Load resume ---
@st.cache_data
def load_resume_text():
    with open("txtresume.txt", "r", encoding="utf-8") as f:
        return f.read()

# --- Simple retrieval (placeholder for now) ---
def retrieve_relevant_text(question, resume_text, max_len=500):
    return resume_text[:max_len]

# --- LLM inference ---
def generate_answer(llm, question, context):
    prompt = (
        "You are a helpful assistant. Use the following resume snippet to answer the question.\n\n"
        f"Resume snippet:\n{context}\n\n"
        f"Question: {question}\n"
        "Answer:"
    )
    output = llm(prompt, max_tokens=256, stop=["\n\n"])
    return output["choices"][0]["text"].strip()

# --- Streamlit App ---
st.title("🤖 Resume Q&A with TinyLlama")

# Load resume
resume_text = load_resume_text()

# --- Model loading UI ---
if "llm" not in st.session_state:
    st.session_state.llm = None

if st.session_state.llm is None:
    if st.button("📥 Load Model"):
        load_model()
    st.warning("👆 Load the model first to start asking questions.")
else:
    # Question input and answer
    question = st.text_input("Ask a question about your resume:")
    if question:
        context = retrieve_relevant_text(question, resume_text)
        answer = generate_answer(st.session_state.llm, question, context)
        st.markdown(f"### Answer:\n{answer}")
#########################################################################################################################



# Email me function

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
def send_email(name, email, input_message):
    # Email configurations
    sender_email = "ericrossfu@yahoo.com"  # Replace with your Yahoo email
    receiver_email = "ericrossfu@yahoo.com"  # Replace with your Yahoo email

    person_who_inquired_email = email
    
    app_specific_password = "qshbgubfeexbmekh"  # Replace with your Yahoo app-specific password
    smtp_server = "smtp.mail.yahoo.com"  # Yahoo SMTP server
    smtp_port = 587  # Use 587 for TLS/STARTTLS or 465 for SSL
    
    # Email content
    subject = "Streamlit Contact Request!"
    message = f"Name: {name}\nEmail: {email}\nJob Opportunity Description:\n\n{input_message}"
    
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
    message2 = f"Hey {name},\n\nI appreciate hearing from you.\nThis is an automated reply.\nThe best way to reach me is 7135404528.\n\n\nBest,\nEric Ross Fu\nData Scientist at Avance Biosciences"
    
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

    
    # Display confirmation
    st.write('Thank you for reaching out! Your inquiry has been sent.')


# Contact me Function
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.title('Contact Me')
    
# Get user input for name
name = st.text_input('Name:', '')

# Get user input for email
email = st.text_input('Email Address:', '')

# Get user input for job opportunity description
input_message = st.text_area('Message:', '')

# Add a "Send" button to send the email
if st.button('Send'):
    # Send email with user details
    send_email(name, email, input_message)
