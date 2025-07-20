# InitialExtractor.py

import streamlit as st

st.set_page_config(page_title="Initial Extractor", layout="centered")

st.title("🔠 Initial Extractor")

# User input
full_name = st.text_input("Enter your full name (e.g., John A Smith):")

if full_name:
    # Clean and split the name
    parts = full_name.strip().split()
    
    # Extract initials
    initials = "".join([part[0].upper() for part in parts if part])
    
    # Display
    st.markdown("## 🧾 Extracted Initials")
    st.success(f"**{initials}**")
