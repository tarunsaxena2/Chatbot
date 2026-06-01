pip install openai
import warnings
warnings.filterwarnings("ignore")

from openai import OpenAI

client = OpenAI(api_key="")

print("🤖 Mallika AI Chatbot")
print("Type 'exit' to stop.\n")

messages = []

while True:
    
    user = input("You : ")

    if user.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user
    })

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    chatbot_reply = response.choices[0].message.content

    print("ChatBot :", chatbot_reply)

    messages.append({
        "role": "assistant",
        "content": chatbot_reply
    })
