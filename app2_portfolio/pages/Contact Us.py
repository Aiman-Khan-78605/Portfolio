import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Us")
df=pandas.read_csv("topic.csv")


with st.form(key="email_form"):
    user_email=st.text_input("Your email_address")
    raw_message=st.text_area("Your Message")
    message=f"""\
Subject:New email from {user_email}

From:{user_email}
{raw_message}
"""
    button=st.form_submit_button("Submit")
    if(button):
        send_email(message)
        st.info("Your email was sent successfully")