from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Zero Shot promptin: Directly giving the instruction to the model
SYSTEM_PROMPT = "You should only and only answer the coding related question. Do not answer anything else. Your name is alexa. If user asks something else other than coding, Just say sorry "

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey There, My name is Sunny. Who are you"}
    ]
)

print(response.choices[0].message.content)

# 1. Zero Shot prompting: The model is given a direct question or task with prior examples.
