# PhoneFormatter.py

import streamlit as st
import re

st.set_page_config(page_title="Phone Number Formatter", layout="centered")
st.title("📞 Phone Number Formatter")

# Input from user
phone_input = st.text_input("Enter a 10-digit phone number:")

# Extract only digits
digits = re.sub(r'\D', '', phone_input)

if digits:
    if len(digits) == 10:
        formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
        st.success(f"📱 Formatted Number: `{formatted}`")
    else:
        st.error("❌ Please enter exactly 10 digits.")
