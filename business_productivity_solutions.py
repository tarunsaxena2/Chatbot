!pip install openai

from openai import OpenAI

client = OpenAI(api_key="")

def business_bot(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a powerful business productivity AI assistant. Help with emails, planning, marketing, automation, and business ideas."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

while True:
    user = input("You: ")
    if user.lower() in ["exit", "quit"]:
        break
    print("Bot:", business_bot(user))
