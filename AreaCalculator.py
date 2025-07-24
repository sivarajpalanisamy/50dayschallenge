# AreaCalculator.py

import streamlit as st
import math
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visual Area Calculator", layout="centered")
st.title("📐 Visual Area Calculator")

# Unit selection
unit = st.selectbox("Choose units of measurement:", ["cm²", "m²", "in²", "ft²"])

# Column layout
col1, col2 = st.columns(2)

with col1:
    # Shape selection and inputs
    shape = st.selectbox("Choose a shape:", ["Circle", "Rectangle", "Triangle"])

    if shape == "Circle":
        radius = st.number_input("Enter radius:", min_value=0.0, format="%.2f")
    elif shape == "Rectangle":
        length = st.number_input("Enter length:", min_value=0.0, format="%.2f")
        width = st.number_input("Enter width:", min_value=0.0, format="%.2f")
    elif shape == "Triangle":
        base = st.number_input("Enter base:", min_value=0.0, format="%.2f")
        height = st.number_input("Enter height:", min_value=0.0, format="%.2f")

with col2:
    def draw_circle(radius):
        fig, ax = plt.subplots()
        circle = plt.Circle((0, 0), radius, fill=False, edgecolor='blue', linewidth=2)
        ax.add_patch(circle)
        ax.set_xlim(-radius * 1.5, radius * 1.5)
        ax.set_ylim(-radius * 1.5, radius * 1.5)
        ax.set_aspect('equal')
        ax.text(0, -0.1, f"r = {radius}", fontsize=12, ha='center')
        ax.axis('off')
        st.pyplot(fig)

    def draw_rectangle(length, width):
        fig, ax = plt.subplots()
        ax.plot([0, length, length, 0, 0], [0, 0, width, width, 0], color='green', linewidth=2)
        ax.text(length / 2, -0.5, f"L = {length}", ha='center')
        ax.text(-0.5, width / 2, f"W = {width}", va='center', rotation='vertical')
        ax.set_xlim(-1, length + 1)
        ax.set_ylim(-1, width + 1)
        ax.set_aspect('equal')
        ax.axis('off')
        st.pyplot(fig)

    def draw_triangle(base, height):
        fig, ax = plt.subplots()
        ax.plot([0, base, 0, 0], [0, 0, height, 0], color='red', linewidth=2)
        ax.text(base / 2, -0.5, f"B = {base}", ha='center')
        ax.text(-0.5, height / 2, f"H = {height}", va='center', rotation='vertical')
        ax.set_xlim(-1, base + 1)
        ax.set_ylim(-1, height + 1)
        ax.set_aspect('equal')
        ax.axis('off')
        st.pyplot(fig)

    # Perform calculation & show output
    if shape == "Circle" and "radius" in locals() and radius > 0:
        area = math.pi * radius ** 2
        st.success(f"🟠 Area of Circle: {area:.2f} {unit}")
        draw_circle(radius)

    elif shape == "Rectangle" and "length" in locals() and "width" in locals() and length > 0 and width > 0:
        area = length * width
        st.success(f"🟦 Area of Rectangle: {area:.2f} {unit}")
        draw_rectangle(length, width)

    elif shape == "Triangle" and "base" in locals() and "height" in locals() and base > 0 and height > 0:
        area = 0.5 * base * height
        st.success(f"🔺 Area of Triangle: {area:.2f} {unit}")
        draw_triangle(base, height)
