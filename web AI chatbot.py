pip install openai
from openai import OpenAI

# OpenAI API Key
client = OpenAI(api_key="")

print("🤖 Mallika AI Chatbot")
print("Type 'exit' to stop.\n")

messages = []

while True:
    
    # User Input
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot Closed.")
        break

    # Save User Message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # OpenAI Response
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    ai_response = response.choices[0].message.content

    # Print AI Response
    print(f"\nMallika AI: {ai_response}\n")

    # Save Assistant Message
    messages.append({
        "role": "assistant",
        "content": ai_response
    })