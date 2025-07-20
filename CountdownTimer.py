# CountdownTimer.py

import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer", layout="centered")

st.title("⏳ Countdown Timer with Pause, Resume, Reset")

# --- Initialize session state variables ---
if "count" not in st.session_state:
    st.session_state.count = 10
if "running" not in st.session_state:
    st.session_state.running = False
if "paused" not in st.session_state:
    st.session_state.paused = False


# --- Define control buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ Start"):
        st.session_state.running = True
        st.session_state.paused = False

with col2:
    if st.button("⏸️ Pause"):
        st.session_state.paused = True

with col3:
    if st.button("🔄 Reset"):
        st.session_state.count = 10
        st.session_state.running = False
        st.session_state.paused = False

# --- Countdown display area ---
placeholder = st.empty()

# --- Run countdown only when not paused ---
if st.session_state.running and not st.session_state.paused:
    if st.session_state.count >= 0:
        placeholder.markdown(f"# ⏱️ {st.session_state.count}")
        time.sleep(1)
        st.session_state.count -= 1
        st.rerun()
    else:
        st.session_state.running = False
        placeholder.markdown("## ✅ Time's up!")
elif st.session_state.paused:
    placeholder.markdown(f"# ⏸️ Paused at {st.session_state.count}")
else:
    placeholder.markdown(f"# ⏱️ {st.session_state.count}")
