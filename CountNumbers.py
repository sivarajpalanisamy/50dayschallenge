import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Number Counter Dashboard", layout="centered")

st.title("🔢 Number Counter Dashboard")
st.markdown("Enter a list of numbers and see how many are positive, negative, or zero.")

# Get input from user
user_input = st.text_input("📥 Enter numbers (comma-separated)", placeholder="e.g. 4, -2, 0, 7, -5")

if user_input:
    try:
        numbers = [int(num.strip()) for num in user_input.split(",")]

        # Count
        positive_count = sum(1 for num in numbers if num > 0)
        negative_count = sum(1 for num in numbers if num < 0)
        zero_count = sum(1 for num in numbers if num == 0)

        # Dashboard-style metrics
        st.markdown("## 📊 Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("Positive", positive_count, f"+{positive_count}")
        col2.metric("Negative", negative_count, f"-{negative_count}")
        col3.metric("Zero", zero_count)

        # Matplotlib bar chart
        st.markdown("## 📈 Visualization")

        fig, ax = plt.subplots()
        categories = ['Positive', 'Negative', 'Zero']
        counts = [positive_count, negative_count, zero_count]
        colors = ['green', 'red', 'gray']

        bars = ax.bar(categories, counts, color=colors)
        ax.set_ylabel("Count")
        ax.set_title("Number Type Distribution")

        # Add value labels on top
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # offset text upward
                        textcoords="offset points",
                        ha='center', va='bottom')

        st.pyplot(fig)

    except ValueError:
        st.error("❌ Please enter only integers separated by commas.")
