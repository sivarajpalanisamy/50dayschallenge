# SimpleCipher.py

import streamlit as st

st.set_page_config(page_title="Simple Cipher", layout="centered")

st.title("🔐 Simple Cipher - Shift Letters by 1")

# User input
text = st.text_input("Enter a word or sentence:")

def shift_letter(char):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + 1) % 26 + base)
    return char  # non-letter characters are unchanged

if text:
    ciphered = "".join(shift_letter(c) for c in text)

    st.markdown("## 🔁 Encrypted Output")
    st.success(ciphered)
