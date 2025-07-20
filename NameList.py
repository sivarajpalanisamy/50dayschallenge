# NameList.py

import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Name List", layout="centered")

st.title("📋 Name List")
st.markdown("Enter 5 names below. We'll show you each name and how many characters it has.")

# Input fields for 5 names
name1 = st.text_input("Name 1")
name2 = st.text_input("Name 2")
name3 = st.text_input("Name 3")
name4 = st.text_input("Name 4")
name5 = st.text_input("Name 5")

names = [name1, name2, name3, name4, name5]

# Only proceed if all names are filled
if all(names):
    name_lengths = [len(name) for name in names]

    # Display names and their lengths
    st.markdown("## 📝 Name Lengths")
    for name, length in zip(names, name_lengths):
        st.write(f"**{name}** has **{length}** characters.")

    # Plot with matplotlib
    st.markdown("## 📊 Name Length Chart")
    fig, ax = plt.subplots()
    ax.bar(names, name_lengths, color='purple')
    ax.set_ylabel("Length")
    ax.set_title("Length of Each Name")

    # Add value labels
    for bar in ax.patches:
        height = bar.get_height()
        ax.annotate(f"{int(height)}",
                    (bar.get_x() + bar.get_width() / 2, height),
                    ha='center', va='bottom', fontsize=10)

    st.pyplot(fig)
else:
    st.info("👉 Please enter all 5 names to continue.")