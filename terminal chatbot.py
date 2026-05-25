pip install openai
import warnings
warnings.filterwarnings("ignore")

from openai import OpenAI

# OpenAI API Key
client = OpenAI(api_key="")

print("🤖 Mallika AI Chatbot")
print("Type 'exit' to stop.\n")

messages = []

while True:
    
    user = input("You : ")

    if user.lower() == "exit":
        break

    # Store user message
    messages.append({
        "role": "user",
        "content": user
    })

    # Generate response
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    chatbot_reply = response.choices[0].message.content

    # Print chatbot response
    print("ChatBot :", chatbot_reply)

    # Store assistant response
    messages.append({
        "role": "assistant",
        "content": chatbot_reply
    })