# SumCalculator.py

import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sum Calculator", layout="centered")

st.title("➕ Sum Calculator")
st.markdown("Enter a number `n` to find the sum of all numbers from 1 to `n` using a loop.")

# Get input from user
n = st.number_input("Enter a positive integer", min_value=1, step=1)

if n:
    # Loop to calculate sum
    total_sum = 0
    cumulative = []  # Store cumulative sums for plotting
    for i in range(1, n + 1):
        total_sum += i
        cumulative.append(total_sum)

    # Dashboard-style summary
    st.markdown("## 📊 Summary")
    st.metric("Sum from 1 to n", total_sum)

    # Plotting the cumulative sum
    st.markdown("## 📈 Cumulative Sum Visualization")
    fig, ax = plt.subplots()
    ax.plot(range(1, n + 1), cumulative, marker='o', linestyle='-', color='blue')
    ax.set_title("Cumulative Sum from 1 to n")
    ax.set_xlabel("Number")
    ax.set_ylabel("Cumulative Sum")
    ax.grid(True)

    st.pyplot(fig)
