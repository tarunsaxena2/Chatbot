from openai import OpenAI

client = OpenAI(api_key="")
import re

# Simple keyword-based filter for Data Science topics
data_science_keywords = [
    "data", "machine learning", "ml", "ai", "artificial intelligence",
    "deep learning", "python", "pandas", "numpy", "statistics",
    "regression", "classification", "clustering", "data analysis",
    "visualization", "matplotlib", "seaborn", "model", "algorithm"
]

def is_data_science_question(question):
    question = question.lower()
    return any(keyword in question for keyword in data_science_keywords)
	
def data_science_assistant(user_input):

    if not is_data_science_question(user_input):
        return "Sorry, I can only answer Data Science related questions."

    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # ✅ Fixed model name
        messages=[
            {"role": "system", "content": "You are a helpful Data Science assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content
	
# Take first input from user
user_input = input("Ask your Data Science question: ")

while True:

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    answer = data_science_assistant(user_input)
    print("Assistant:", answer)

    # Ask for next input
    user_input = input("\nAsk your Data Science question (or type 'exit'): ")