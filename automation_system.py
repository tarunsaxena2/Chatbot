!pip install -U openai

from openai import OpenAI

client = OpenAI(api_key="")

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a short automation workflow."
)

print(response.output_text)

import pandas as pd
from openai import OpenAI

data = {
    "feedback": [
        "Great service and fast delivery",
        "Product quality is poor",
        "Customer support was very helpful"
    ]
}

df = pd.DataFrame(data)
df.to_csv("customers.csv", index=False)


df = pd.read_csv("customers.csv")

client = OpenAI(api_key="")

for text in df["feedback"]:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Summarize this feedback: {text}"
    )
    print(response.output_text)
