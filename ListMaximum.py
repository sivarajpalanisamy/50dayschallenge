# ListMaximum.py

import streamlit as st

st.set_page_config(page_title="List Maximum Finder", layout="centered")

st.title("🔍 List Maximum (Without using max())")

st.markdown("Enter a list of numbers separated by commas:")

# User input
user_input = st.text_input("📥 Input numbers (e.g., 12, 5, 8, 22, 3):")

if user_input:
    try:
        numbers = [int(num.strip()) for num in user_input.split(",")]
        
        # Find max using a loop
        largest = numbers[0]
        for num in numbers[1:]:
            if num > largest:
                largest = num

        # Show result
        st.markdown("## ✅ Result")
        st.success(f"The largest number is: **{largest}**")

    except ValueError:
        st.error("❌ Please enter only integers separated by commas.")
