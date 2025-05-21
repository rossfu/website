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


# AI #########################################################################################################################
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
from sentence_transformers import SentenceTransformer
import faiss
import os

# Title
st.title("🤖 Would you like to ask AI about my resume?")

# 1. Cache the embedder
@st.cache_resource
def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

# 2. Load and cache the resume text
@st.cache_data
def load_resume_text():
    with open("txtresume.txt", "r", encoding="utf-8") as f:
        return f.read()

# 3. Use cached embedder and resume text to generate vectors + FAISS index
def prepare_index(embedder, resume_text):
    chunks = [chunk.strip() for chunk in resume_text.split("\n\n") if chunk.strip()]
    vectors = embedder.encode(chunks)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return chunks, index

# 4. Cache the LLM
@st.cache_resource
def load_llm():
    return pipeline("text2text-generation", model="google/flan-t5-small")

# 5. Initialize state
if "model_loaded" not in st.session_state:
    st.session_state.model_loaded = False

# 6. Load button
if not st.session_state.model_loaded:
    if st.button("Yes!"):
        with st.spinner("Loading model and embedding resume..."):
            embedder = load_embedder()
            resume_text = load_resume_text()
            chunks, index = prepare_index(embedder, resume_text)

            # Save to session state
            st.session_state.embedder = embedder
            st.session_state.chunks = chunks
            st.session_state.index = index
            st.session_state.rag_model = load_llm()
            st.session_state.model_loaded = True
        st.experimental_rerun()

# 7. If model is ready
if st.session_state.model_loaded:
    st.success("✅ Model and resume loaded.")
    user_input = st.text_input("💬 What would you like to know about my resume?")

    if st.button("Ask") and user_input.strip():
        with st.spinner("Thinking..."):
            user_input_vec = st.session_state.embedder.encode([user_input], convert_to_tensor=False)
            D, I = st.session_state.index.search(user_input_vec, k=3)
            context = "\n".join([st.session_state.chunks[i] for i in I[0]])

            prompt = (
                "You are an intelligent and helpful assistant answering questions about the following resume.\n"
                "Resume content:\n"
                f"{context}\n\n"
                "Instruction: Given the above resume, respond to the user's message below. "
                "If the message is not a question, respond naturally and casually as if continuing a conversation. "
                "If you don’t know the answer based on the resume, say so honestly.\n\n"
                f"User: {user_input}\n"
                "Answer:"
            )

            answer = st.session_state.rag_model(prompt, max_length=200)[0]['generated_text']
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
