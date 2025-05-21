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
st.title("Welcome to Eric Fu's Website!")


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
    
    # Read the file in binary mode
    with open("Eric Fu Resume 2025.pdf", "rb") as f:
        pdf_data = f.read()
    
    # Download button
    st.download_button(
        label="Download my Resume",
        data=pdf_data,
        file_name="resume.pdf",
        mime="application/pdf"
    )


st.write("")
st.write("")
st.write("")
st.write("")



# AI #########################################################################################################################
import streamlit as st
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
from sentence_transformers import SentenceTransformer
import faiss
import os

MODEL_NAME = "google/flan-t5-small"

@st.cache_resource
def load_resume_data():
    with open("txtresume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()
    chunks = [resume_text[i:i+400] for i in range(0, len(resume_text), 400)]
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    chunk_embeddings = embedder.encode(chunks, convert_to_tensor=False)
    index = faiss.IndexFlatL2(len(chunk_embeddings[0]))
    index.add(chunk_embeddings)
    return embedder, chunks, index

@st.cache_resource
def load_llm():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return pipeline("text2text-generation", model=model, tokenizer=tokenizer)

st.title("💼 Ask Questions About My Resume")

if "model_loaded" not in st.session_state:
    st.session_state.model_loaded = False

if not st.session_state.model_loaded:
    if st.button("🚀 Load Model"):
        with st.spinner("Loading model and embedding resume..."):
            st.session_state.rag_model = load_llm()
            st.session_state.embedder, st.session_state.chunks, st.session_state.index = load_resume_data()
            st.session_state.model_loaded = True
else:
    # Once model is loaded, button and "Model loaded!" message disappear automatically
    question = st.text_input("What would you like to know about my resume?")
    if st.button("Ask"):
        with st.spinner("Generating answer..."):
            question_vec = st.session_state.embedder.encode([question], convert_to_tensor=False)
            D, I = st.session_state.index.search(question_vec, k=3)
            context = "\n".join([st.session_state.chunks[i] for i in I[0]])
            prompt = f"Context: {context}\n\nQuestion: {question}"
            answer = st.session_state.rag_model(prompt, max_length=100)[0]['generated_text']
        st.markdown("### 📌 Answer")
        st.write(answer)

#########################################################################################################################



# Email me function
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
