# TextStatistics.py

import streamlit as st
import re

st.set_page_config(page_title="Text Statistics", layout="centered")
st.title("📊 Text Statistics")

# Text input
paragraph = st.text_area("Enter your paragraph:")

if paragraph:
    # Count characters (with and without spaces)
    char_with_spaces = len(paragraph)
    char_without_spaces = len(paragraph.replace(" ", ""))

    # Count words
    words = paragraph.split()
    word_count = len(words)

    # Count sentences (simple split by punctuation)
    sentences = re.split(r'[.!?]+', paragraph)
    sentences = [s for s in sentences if s.strip()]  # remove empty
    sentence_count = len(sentences)

    # Display stats
    st.markdown("## 📋 Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("📝 Words", word_count)
    col2.metric("📙 Sentences", sentence_count)
    col3.metric("🔠 Characters", char_with_spaces)

    with st.expander("📌 Details"):
        st.write(f"Characters (with spaces): {char_with_spaces}")
        st.write(f"Characters (without spaces): {char_without_spaces}")
        st.write(f"Words: {word_count}")
        st.write(f"Sentences: {sentence_count}")
