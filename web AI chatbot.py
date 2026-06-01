pip install openai
from openai import OpenAI

client = OpenAI(api_key="")

print("🤖 Mallika AI Chatbot")
print("Type 'exit' to stop.\n")

messages = []

while True:
        
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot Closed.")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    ai_response = response.choices[0].message.content


    print(f"\nMallika AI: {ai_response}\n")

    messages.append({
        "role": "assistant",
        "content": ai_response
    })
