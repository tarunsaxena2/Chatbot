

!pip install -q openai

import os

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

print("Intelligent Assistant System")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    try:
        response = client.responses.create(
            model="gpt-5",
            input=user_input
        )

        print("\nAssistant:", response.output_text)
        print()

    except Exception as e:
        print("Error:", e)

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

conversation = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    conversation.append({
        "role": "user",
        "content": user_input
    })

    response = client.responses.create(
        model="gpt-5",
        input=conversation
    )

    assistant_reply = response.output_text

    conversation.append({
        "role": "assistant",
        "content": assistant_reply
    })

    print("\nAssistant:", assistant_reply)
