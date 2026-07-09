import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="")

def generate_grammar_exercise():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Data Science teacher. Your job is to teach concepts through MCQ or fill in the blank questions. Ask only one question."},
            {"role": "user", "content": "Create one Data Science question (MCQ or fill in the blank)."}
        ]
    )
    return completion.choices[0].message.content.strip()

def check_answer(question, user_answer):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Data Science teacher. Evaluate the user's answer."},
            {"role": "user", "content": f"Question: {question}\nAnswer: {user_answer}"}
        ]
    )
    return completion.choices[0].message.content.strip()


def app():
    st.set_page_config(page_title="DS Tutor", page_icon="📊", layout="centered")

    # 🔥 Advanced CSS Styling
    st.markdown("""
    <style>

    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #141e30, #243b55);
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    /* Glass Card Effect */
    .card {
        background: rgba(255, 255, 255, 0.08);
        padding: 25px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin-top: 20px;
    }

    /* Title */
    h1, h2, h3 {
        text-align: center;
        color: #00ffd5;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #00ffd5, #00c6ff);
        color: black;
        border-radius: 12px;
        padding: 10px 25px;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #00c6ff, #0072ff);
        color: white;
    }

    /* Input Box */
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        border: 2px solid #00ffd5;
        background-color: rgba(255,255,255,0.1);
        color: white;
    }

    /* Subtext */
    .subtitle {
        text-align: center;
        color: #ccc;
        font-size: 16px;
    }

    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h1>📊 Data Science Tutor</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Practice MCQs & Improve Concepts with AI</p>", unsafe_allow_html=True)

    # Session state
    if 'exercise' not in st.session_state:
        st.session_state.exercise = None
    if 'user_response' not in st.session_state:
        st.session_state.user_response = ''

    # Card container
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if st.button('🚀 Start Exercise'):
        st.session_state.exercise = generate_grammar_exercise()

    if st.session_state.exercise:
        st.subheader('📝 Exercise')
        st.write(st.session_state.exercise)

        user_response = st.text_input('✍️ Your Answer:', key="response")

        if st.button('✅ Check Answer'):
            if user_response:
                feedback = check_answer(st.session_state.exercise, user_response)
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.subheader('📢 Feedback')
                st.write(feedback)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.error("⚠️ Please enter an answer before checking.")

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    app()