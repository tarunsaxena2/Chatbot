import streamlit as st
import sounddevice as sd
import numpy as np
import wave

# Page config
st.set_page_config(page_title="Audio Recorder", page_icon="🎤", layout="centered")

# 🔥 Advanced CSS Styling
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: white;
    font-family: 'Poppins', sans-serif;
}

/* Title */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #ff4b2b;
}

/* Card */
.card {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 15px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    margin-top: 20px;
    text-align: center;
}

/* Button */
.stButton>button {
    background: linear-gradient(45deg, #ff4b2b, #ff416c);
    color: white;
    border-radius: 12px;
    padding: 12px 25px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.08);
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
}

/* Recording animation */
.recording {
    color: red;
    font-weight: bold;
    animation: blink 1s infinite;
}

@keyframes blink {
    50% { opacity: 0.3; }
}

</style>
""", unsafe_allow_html=True)

# UI Header
st.markdown("<div class='title'>🎤 Audio Recorder App</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

# User Inputs
duration = st.slider("⏱️ Select Recording Duration (seconds)", 5, 30, 10)
sample_rate = 44100

# Record Button
if st.button("🎙️ Start Recording"):
    st.markdown("<div class='recording'>🔴 Recording...</div>", unsafe_allow_html=True)

    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()

    st.success("✅ Recording Complete!")

    output_file = "output.wav"
    with wave.open(output_file, 'w') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

    st.audio(output_file)
    st.success(f"💾 Saved as {output_file}")

st.markdown("</div>", unsafe_allow_html=True)