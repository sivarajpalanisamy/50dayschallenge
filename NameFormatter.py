# NameFormatter.py

import streamlit as st

st.set_page_config(page_title="Name Formatter", layout="centered")

st.title("📝 Name Formatter")

# Input
full_name = st.text_input("Enter your full name (First Last):")

if full_name:
    parts = full_name.strip().split()

    if len(parts) >= 2:
        first = parts[0].capitalize()
        last = " ".join([p.capitalize() for p in parts[1:]])
        last_initial = last[0].upper()

        # Formats
        format1 = f"{first} {last}"
        format2 = f"{last}, {first}"
        format3 = f"{last_initial}. {first}"
        format4 = f"{first.upper()}, {last.upper()}"

        st.markdown("## ✨ Formatted Versions")
        st.write("👉 **First Last**:", format1)
        st.write("👉 **Last, First**:", format2)
        st.write("👉 **Initial Format (L. First)**:", format3)
        st.write("👉 **Uppercase Style (FIRST, LAST)**:", format4)

    else:
        st.warning("⚠️ Please enter at least first and last name.")
