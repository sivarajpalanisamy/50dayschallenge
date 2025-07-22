# EmailUsername.py

import streamlit as st

st.set_page_config(page_title="Email Username Extractor", layout="centered")
st.title("📧 Email Username Extractor")

# User input
email = st.text_input("Enter your email address:")

if email:
    if "@" in email:
        username = email.split("@")[0]
        st.success(f"**Username:** `{username}`")
    else:
        st.error("❌ Please enter a valid email address.")