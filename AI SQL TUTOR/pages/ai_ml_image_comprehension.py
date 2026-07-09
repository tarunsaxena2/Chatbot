import streamlit as st
import requests
import numpy as np
import sounddevice as sd
import io
from scipy.io.wavfile import write
import wave
import openai
from openai import OpenAI
client = OpenAI(api_key="")



def speech_to_text(file_path):
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    st.write("Transcript:")
    st.write(transcription.text)
    return transcription.text


def generate_ai_image():
    prompt = "A futuristic AI system, machine learning concept, high-tech digital brain, modern AI illustration"

    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024"
    )

    image_url = response.data[0].url
    return image_url


def describe_image(image_url):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image in an AI & ML exam style. Use technical terms like neural networks, data, training, etc."},
                    {
                        "type": "image_url",
                        "image_url": {"url": image_url},
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    result = response.choices[0].message.content
    st.write("Model Description:")
    st.write(result)
    return result


def compare_descriptions(model_desc, user_desc):
    st.write(f"Model Description: {model_desc}")
    st.write(f"Your Description: {user_desc}")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI & ML teacher. Evaluate the user's description based on: Use of AI/ML keywords"),
            },
            {
                "role": "user",
                "content": f"Model: {model_desc}\nUser: {user_desc}\nGive feedback.",
            },
        ],
    )

    feedback = completion.choices[0].message.content
    st.subheader("Feedback")
    st.write(feedback)



def app():
    st.header('AI Image Comprehension')
    st.write('Describe an AI-generated image in 30 seconds.')

    if 'image_shown' not in st.session_state:
        st.session_state.image_shown = False
    if 'image_generated' not in st.session_state:
        st.session_state.image_generated = False

    # Start button
    if st.button('Start'):
        st.session_state.image_shown = True
        st.session_state.image_generated = False

    if st.session_state.image_shown:

        # Generate AI Image
        if not st.session_state.image_generated:
            image_url = generate_ai_image()
            st.session_state.image_url = image_url
            st.session_state.image_generated = True

        st.image(st.session_state.image_url, caption='Describe this AI/ML image.')

        st.write(
            "You have 30 seconds. Focus on AI/ML concepts like neural networks, data, models, training, automation."
        )

        if st.button('Start Talking'):
            duration = 30
            sample_rate = 44100

            st.write('Recording...')
            recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
            sd.wait()
            st.write('Done recording.')

            output_file = "output.wav"
            with wave.open(output_file, 'w') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(sample_rate)
                wf.writeframes(recording.tobytes())

            user_description = speech_to_text(output_file)
            model_description = describe_image(st.session_state.image_url)
            compare_descriptions(model_description, user_description)