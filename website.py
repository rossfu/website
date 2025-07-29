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
#audio_file = open('Survivor - Eye Of The Tiger (Official HD Video).mp3', 'rb')
#st.audio(audio_file, format='audio/mp3', start_time=0)



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
import streamlit as st
import openai
import time

# Load credentials
openai.api_key = st.secrets["OPENAI_API_KEY"]
assistant_id = st.secrets["OPENAI_ASSISTANT_ID"]

st.title("🤖 Ask AI about my Resume")

# Layout: text input and submit button
user_input = st.text_input("Ask away")
submit = st.button("Send")

# Rate limiting setup
if "last_query_time" not in st.session_state:
    st.session_state.last_query_time = 0

if submit:
    if time.time() - st.session_state.last_query_time < 10:
        st.warning("Please wait a few seconds before asking another question.")
        st.stop()

    if len(user_input) > 500:
        st.warning("500 character limit")
        st.stop()

    st.session_state.last_query_time = time.time()

    with st.spinner("Thinking..."):
        # Create or reuse thread
        if "thread_id" not in st.session_state:
            thread = openai.beta.threads.create()
            st.session_state.thread_id = thread.id
        else:
            thread = openai.beta.threads.retrieve(st.session_state.thread_id)

        # Add user message
        openai.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input
        )

        # Run assistant
        run = openai.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )

        # Poll for response
        while True:
            run_status = openai.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run_status.status == "completed":
                break
            elif run_status.status == "failed":
                st.error("Assistant failed to respond.")
                break
            time.sleep(1)

        # Display answer
        messages = openai.beta.threads.messages.list(thread_id=thread.id)
        response = messages.data[0].content[0].text.value
        st.success(response)

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
st.title('📧 Contact Me')
    
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
