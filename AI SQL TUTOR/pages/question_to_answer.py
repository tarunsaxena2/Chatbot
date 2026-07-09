import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="")

# ----------- ADVANCED CSS -----------
def load_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&family=Poppins:wght@300;400;500&display=swap');

    /* Global */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at top, #0f2027, #203a43, #2c5364);
        color: white;
    }

    /* Glass container */
    .main-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 8px 40px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.1);
        animation: fadeIn 1s ease-in-out;
    }

    /* Neon Title */
    h2, h1 {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        color: #00e6ff;
        text-shadow: 0 0 10px #00e6ff, 0 0 20px #00e6ff;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #00f2fe, #4facfe);
        border: none;
        border-radius: 12px;
        padding: 10px 25px;
        color: white;
        font-weight: 600;
        transition: 0.3s;
        box-shadow: 0 0 15px rgba(0,242,254,0.6);
    }

    .stButton>button:hover {
        transform: scale(1.07);
        box-shadow: 0 0 25px rgba(0,242,254,1);
    }

    /* Input (SQL editor feel) */
    textarea, input {
        background: rgba(0,0,0,0.6) !important;
        color: #00ff9f !important;
        font-family: monospace !important;
        border-radius: 10px !important;
        border: 1px solid #00ff9f !important;
        padding: 12px !important;
    }

    /* Question box */
    .question-box {
        background: rgba(255,255,255,0.07);
        padding: 15px;
        border-left: 5px solid #00e6ff;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    /* Feedback box */
    .feedback-box {
        background: rgba(0,255,150,0.08);
        border-left: 5px solid #00ff9f;
        padding: 15px;
        border-radius: 10px;
    }

    /* Error */
    .stAlert {
        border-radius: 10px;
    }

    /* Animation */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }

    </style>
    """, unsafe_allow_html=True)

# ----------- AI FUNCTIONS -----------
def generate_random_sentence():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a database teacher."},
            {"role": "user", "content": "Generate a SQL query problem."}
        ]
    )
    return completion.choices[0].message.content.strip()

def verify_translation(original, translation):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Check SQL query and give feedback."},
            {"role": "user", "content": f"Question: {original}\nQuery: {translation}"}
        ]
    )
    return completion.choices[0].message.content.strip()

# ----------- MAIN APP -----------
def app():
    load_css()

    st.markdown("<h1>💻 SQL AI Trainer</h1>", unsafe_allow_html=True)

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    st.write("🚀 Practice SQL with AI-powered feedback")

    if 'generated_sentence' not in st.session_state:
        st.session_state.generated_sentence = None

    if st.button('⚡ Generate Question'):
        st.session_state.generated_sentence = generate_random_sentence()

    if st.session_state.generated_sentence:
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.subheader("📌 SQL Question")
        st.write(st.session_state.generated_sentence)
        st.markdown('</div>', unsafe_allow_html=True)

        user_query = st.text_area("💡 Write your SQL query here:", height=150)

        if st.button('✅ Verify Answer'):
            if user_query:
                feedback = verify_translation(st.session_state.generated_sentence, user_query)

                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.subheader("🧠 AI Feedback")
                st.write(feedback)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("⚠️ Please enter a SQL query first.")

    st.markdown('</div>', unsafe_allow_html=True)