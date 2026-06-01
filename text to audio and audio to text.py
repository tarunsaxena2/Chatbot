pip install config

import openai

import config

import openai
import config

openai.api_keys = ""

from openai import OpenAI
client = OpenAI(api_key = openai.api_keys)

#Text to Audio

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello, I am Tarun Saxena, student of Hindustan College and pursuing B.Tech in Computer Science.")
response.stream_to_file("output.mp3")

# Audio to Text
audio_file = open ("/content/output.mp3","rb")
response = client.audio.transcriptions.create(
    model="whisper-1",
    file = audio_file
)

print(response.text)

image_url = response.data[0].url

print(f"Your image is ready at : {image_url}")

