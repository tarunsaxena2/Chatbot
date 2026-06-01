!pip install openAI

import openai

openai.api_key = ""
from google.colab import drive

drive.mount('/content/drive',force_remount = True)

file_path = '/content/drive/MyDrive/GAI WORKSPHOP/Hindustan-College-of-Science-Technology20260227-1.txt'

with open(file_path, 'r') as file:
  content = file.read()

len(content)


base_instruction = '''You are an AI assistant that extracts accurate information from a NIRF PDF.
- Use exact facts and figures only
- Do not assume or add external information
- If data is missing, say: "I don't know"
- Show step-by-step calculations when required
- Keep responses clear and structured '''

#QUESTION 1

question = "The doc shared is of which year?"

prompt = base_instruction+"\n\n" + "Question : {0}".format(question) + "\n\n" + "Transcript : \n {0}".format(content)

message = [{"role" : "user", "content" : prompt}]

chat_response = openai.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=message,
    max_tokens=100,
    temperature = 0.5,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0)
print(chat_response.choices[0].message.content)

#QUESTION 2

question = "No. of student enrollled in the session 2025-2026. Give me detailed breakdown."

prompt = base_instruction+"\n\n" + "Question : {0}".format(question) + "\n\n" + "Transcript : \n {0}".format(content)

message = [{"role" : "user", "content" : prompt}]

chat_response = openai.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=message,
    max_tokens=200,
    temperature = 0.5,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0)
print(chat_response.choices[0].message.content)

#QUESTION 3

question = "Is there a percentage increase in number of students enrolled in consecutive years or not. Give the complete calculation."

prompt = base_instruction+"\n\n" + "Question : {0}".format(question) + "\n\n" + "Transcript : \n {0}".format(content)

message = [{"role" : "user", "content" : prompt}]

chat_response = openai.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=message,
    max_tokens=500,
    temperature = 0.5,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0)
print(chat_response.choices[0].message.content)

#QUESTION 4

question = "Give me the complete faculty details who as designation as professor."

prompt = base_instruction+"\n\n" + "Question : {0}".format(question) + "\n\n" + "Transcript : \n {0}".format(content)

message = [{"role" : "user", "content" : prompt}]

chat_response = openai.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=message,
    max_tokens=500,
    temperature = 0.5,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0)
print(chat_response.choices[0].message.content)

#QUESTION 5

question = "Number of total B.Tech students, M.tech students, PhD holders across all years."

prompt = base_instruction+"\n\n" + "Question : {0}".format(question) + "\n\n" + "Transcript : \n {0}".format(content)

message = [{"role" : "user", "content" : prompt}]

chat_response = openai.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=message,
    max_tokens=700,
    temperature = 0.5,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0)
print(chat_response.choices[0].message.content)

#QUESTION 6

question = "Give me the detail breakdown of fee detail for B.Tech"

prompt = base_instruction+"\n\n" + "Question : {0}".format(question) + "\n\n" + "Transcript : \n {0}".format(content)

message = [{"role" : "user", "content" : prompt}]

chat_response = openai.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=message,
    max_tokens=750,
    temperature = 0.5,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0)
print(chat_response.choices[0].message.content)
