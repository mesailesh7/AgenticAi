from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an expert in Maths and only and only answer maths related questions"},
        {"role": "user", "content": "Hey There, My name is Sunny. Who are you"}
    ]
)

print(response.choices[0].message.content)
