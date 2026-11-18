
import streamlit as st

st.set_page_config(
    page_title="My Marks Calculator",
    page_icon="📚",
    layout="centered"
)

st.title("📚 My Marks Calculator")
st.subheader("Calculate Your Exam Results")

st.write("Enter your marks (0–100) for each subject.")

subjects = [
    "Tamil",
    "English",
    "Maths",
    "Science",
    "Social",
    "G.K",
    "Computer",
    "Tamil Grammar",
    "English Grammar"
]

marks = {}

for subject in subjects:
    marks[subject] = st.number_input(
        subject,
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

if st.button("Calculate My Result", use_container_width=True):

    total = sum(marks.values())
    percentage = total / 9

    st.divider()

    st.success(f"Total Marks: {total} / 900")

    st.metric("Your Percentage", f"{percentage:.2f}%")

    if percentage >= 90:
        st.balloons()
        st.success("🏆 Excellent! You scored 90% or above!")

    elif percentage >= 75:
        st.success("🌟 Very Good! Keep it up!")

    elif percentage >= 50:
        st.info("👍 Good effort! Keep practising!")

    else:
        st.warning("📖 Keep studying. You can improve!")

if st.button("Reset Marks", use_container_width=True):
    st.rerun()

st.caption("Made with Python ❤️")
