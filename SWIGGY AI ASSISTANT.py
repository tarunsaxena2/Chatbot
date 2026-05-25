import openai

openai.api_key = ""
messages = [
    {
        "role": "system",
        "content": "You are an AI assistant that classifies food delivery reviews into three categories: Good, Okay, or Bad"
    },
    {
        "role": "user",
        "content": " REVIEW 1 : The paneer dish was nither  too good nor too bad . It's a one  time experience . Review 2: THE FOOD AND THE PLACE WAS AMAZING  WILL DEFINETLY COME HERE  AGAIN  .  Review 3 : The ambience of the resturant was good but the food was pathetic which spoiled my whole experience "
    }
]
messages
chat_response =  openai.chat.completions.create(
    model ="gpt-3.5-turbo-16k",
    messages=messages,
    max_tokens=1000,
    temperature=0.5,
    n=2,
  stop='Good',
  frequency_penalty=00,
  presence_penalty=0

)
chat_response.choices[0].message.content