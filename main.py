import streamlit as st
from app.utils import transcribe_voice, evaluate_answer
from app.feedback import generate_feedback
from app.question_bank import get_questions

st.set_page_config(page_title="AI-Powered Virtual Interviewer", layout="centered")

def main():
    st.title("AI-Powered Virtual Interviewer")
    st.sidebar.title("Menu")
    domain = st.sidebar.selectbox("Select Domain", ["General", "Technical", "HR", "Management"])

    st.write("### Mock Interview")
    questions = get_questions(domain)
    scores = []

    for idx, question in enumerate(questions):
        st.write(f"**Q{idx + 1}: {question}**")
        response = st.text_area(f"Your answer for Q{idx + 1}")
        if st.button(f"Evaluate Q{idx + 1}"):
            score, feedback = evaluate_answer(response, question)
            st.write(f"**Score:** {score}/10")
            st.write(f"**Feedback:** {feedback}")
            scores.append(score)

    if len(scores) > 0:
        st.write(f"### Final Score: {sum(scores)}/{len(scores) * 10}")
        tips = generate_feedback(scores)
        st.write("### Tips for Improvement:")
        for tip in tips:
            st.write(f"- {tip}")

if __name__ == "__main__":
    main()
