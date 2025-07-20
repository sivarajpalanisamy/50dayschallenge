# WordReverser.py

import streamlit as st
import nltk
from nltk.corpus import words
import html

# Download word list if not available
try:
    nltk.data.find("corpora/words")
except LookupError:
    nltk.download("words")

english_words = set(words.words())

st.set_page_config(page_title="Word Reverser", layout="centered")
st.title("🔁 Word Reverser + Meaning Detector")

sentence = st.text_input("Enter a sentence:")

if sentence:
    word_list = sentence.split()
    reversed_styled_words = []
    detected_words = []

    for word in word_list:
        reversed_word = word[::-1]
        safe_word = html.escape(reversed_word)

        if reversed_word.lower() in english_words:
            styled = f"<u>{safe_word}</u>"
            detected_words.append(reversed_word)
        else:
            styled = safe_word

        reversed_styled_words.append(styled)

    final_output = " ".join(reversed_styled_words)

    st.markdown("## 🔄 Reversed Sentence")
    st.markdown(f"<p style='font-size:24px; font-family:monospace'>{final_output}</p>", unsafe_allow_html=True)

    if detected_words:
        st.markdown("### 📝 Explanation")
        st.success(
            f"The following reversed words are valid English words and are underlined: "
            f"**{', '.join(detected_words)}**"
        )
    else:
        st.info("ℹ️ None of the reversed words are valid English words.")
