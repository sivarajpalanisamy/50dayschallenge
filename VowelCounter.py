# VowelCounter.py

import streamlit as st

st.set_page_config(page_title="Vowel Counter", layout="centered")

st.title("🅰️ Vowel Counter & Highlighter")

# Input from user
word = st.text_input("Enter a word:")

if word:
    vowels = "aeiouAEIOU"
    total_chars = len(word)
    vowel_count = 0
    highlighted_word = ""

    for char in word:
        if char in vowels:
            vowel_count += 1
            highlighted_word += f"<span class='emoji-vowel'>{char}</span>"
        else:
            highlighted_word += f"<span class='normal'>{char}</span>"

    # Display counts
    col1, col2 = st.columns(2)
    col1.metric("🔢 Total Characters", total_chars)
    col2.metric("🅰️ Vowel Count", vowel_count)

    # Custom styling to look like 🅰️ emoji
    st.markdown("""
        <style>
        .emoji-vowel {
            display: inline-block;
            background-color: #ff4b4b;
            color: white;
            font-weight: bold;
            font-size: 22px;
            width: 36px;
            height: 36px;
            line-height: 36px;
            text-align: center;
            border-radius: 50%;
            margin: 3px;
        }
        .normal {
            font-size: 22px;
            margin: 3px;
            display: inline-block;
            width: 26px;
            height: 36px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### 🔍 Highlighted Word:")
    st.markdown(f"<div>{highlighted_word}</div>", unsafe_allow_html=True)
