import streamlit as st

st.header("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input("Please type your email address...")
    message = st.text_area("Please type your message")
    button = st.form_submit_button("Submit")