import streamlit as st
from pages import home,question_to_answer,ai_ml_image_comprehension, fill_in_blank

# ----------- ADVANCED CSS -----------
def load_css():
    st.markdown("""
    <style>

    /* Import Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Background with animated gradient */
    .stApp {
        background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1c1c1c);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
        color: white;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Glassmorphism container */
    .block-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: rgba(20, 30, 48, 0.85);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.1);
    }

    /* Sidebar title */
    section[data-testid="stSidebar"] h1 {
        font-size: 22px;
        font-weight: 600;
        color: #ffffff;
        text-align: center;
    }

    /* Radio buttons (menu items) */
    .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .stRadio label {
        background: rgba(255,255,255,0.08);
        padding: 10px 15px;
        border-radius: 12px;
        transition: 0.3s;
        cursor: pointer;
    }

    .stRadio label:hover {
        background: rgba(255,255,255,0.2);
        transform: translateX(5px);
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #00c6ff, #0072ff);
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
        color: white;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 114, 255, 0.4);
    }

    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(0, 114, 255, 0.6);
    }

    /* Input fields */
    input, textarea {
        border-radius: 10px !important;
        border: none !important;
        padding: 10px !important;
        background: rgba(255,255,255,0.08) !important;
        color: white !important;
    }

    /* Headers */
    h1 {
        text-align: center;
        font-weight: 600;
        letter-spacing: 1px;
    }

    h2, h3 {
        color: #f1f1f1;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #1c1c1c;
    }

    ::-webkit-scrollbar-thumb {
        background: #555;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #888;
    }

    /* Fade-in animation */
    .block-container {
        animation: fadeIn 1s ease-in-out;
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }

    </style>
    """, unsafe_allow_html=True)

# ----------- Pages -----------
PAGES = {
    "Home": home,
    "AI & ML Image Comprehension": ai_ml_image_comprehension,
    "Data Science MCQ": fill_in_blank,
    "Question and Answer": question_to_answer
}

# ----------- Main App -----------
def main():
    load_css()

    st.sidebar.title("🚀 Navigation")
    selection = st.sidebar.radio("", list(PAGES.keys()))

    st.title("🤖 AI Learning Dashboard")

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()