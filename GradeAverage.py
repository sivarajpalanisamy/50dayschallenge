# GradeAverage.py

import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Grade Average Dashboard", layout="wide")

st.title("📘 AI Grade Dashboard (Matrix Style Input)")

subjects = ["Machine Learning", "Deep Learning", "NLP", "Computer Vision", "Reinforcement Learning"]
student_cols = st.columns(3)

# ✅ Define the student_data list BEFORE using it
student_data = []

# Matrix-style input: 3 student columns
for idx, col in enumerate(student_cols):
    with col:
        st.markdown(f"### 👤 Student {idx+1}")
        name = st.text_input("Name", key=f"name_{idx}")
        scores = []
        for sub in subjects:
            score = st.number_input(sub, min_value=0, max_value=100, key=f"{sub}_{idx}")
            scores.append(score)
        student_data.append((name, scores))

# ✅ VALIDATION: Check for non-empty names and all scores entered
valid_students = [s for s in student_data if s[0] and all(score > 0 for score in s[1])]

# ✅ Merged Bar Chart for All Students
if valid_students:
    st.markdown("## 📊 Subject-wise Comparison Chart")

    fig, ax = plt.subplots(figsize=(10, 5))
    bar_width = 0.25
    x = list(range(len(subjects)))

    for i, (name, scores) in enumerate(valid_students):
        offset = [xi + bar_width * i for xi in x]
        ax.bar(offset, scores, width=bar_width, label=name)
        for xi, score in zip(offset, scores):
            ax.text(xi, score + 1, f"{int(score)}", ha='center', fontsize=8)

    ax.set_xticks([xi + bar_width for xi in x])
    ax.set_xticklabels(subjects)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Marks")
    ax.set_title("Student Score Comparison")
    ax.legend(title="Students")
    st.pyplot(fig)

else:
    st.warning("📥 Enter names and non-zero scores for each student to view the combined chart.")
