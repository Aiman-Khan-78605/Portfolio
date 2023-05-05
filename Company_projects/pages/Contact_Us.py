import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Us")
df=pandas.read_csv('/Users/aimankhan/Desktop/Python_Projects/Company_projects/topics.csv')
with st.form(key="send_email"):
    user_email = st.text_input("Your email_address")
    option=st.selectbox("What do you want to discuss",df['topic'])
    raw_message = st.text_area("Your Message")
    message = f"""\
    Subject:New email from {user_email}
    Topic {option}
    From:{user_email}
    {raw_message}
    """
    button = st.form_submit_button("Submit")
if (button):
    send_email(message)
    st.info("Your email was sent successfully")