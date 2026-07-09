import streamlit as st

def app():
    # Page config
    st.set_page_config(page_title="CS Tutor", page_icon="💻", layout="centered")

    # Custom CSS styling
    st.markdown("""
        <style>
        body {
            background-color: #0e1117;
        }
        .main {
            background-color: #0e1117;
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .box {
            background-color: #1c1f26;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.title("💻 Computer Science Tutor")

    # Subtitle
    st.markdown("<h4 style='text-align:center; color:gray;'>Enhance your SQL skills with exercises!</h4>", unsafe_allow_html=True)

   


# Run the app
if __name__ == "__main__":
    app()