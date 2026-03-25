# Persona Based prompting
from dotenv import load_dotenv
from openai import OpenAI

import json

load_dotenv()

client = OpenAI()

# Few Shot promptin: Directly giving the instruction to the model and few examples to the model
SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Piyush Garg.
    You are acting on behalf of Piyush Garg who is 25 Years old Tech enthusiast and principle engineer. Your main tech stack and Javascript and Python and You are learning GENAI these days.
    
    Exmaples:
    Q:Hey
    A: Hey, Whats up!
    
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey There, My name is Sunny. Who are you"}
    ]
)

print(response.choices[0].message.content)

# 1.Few shot Prompting: The model is provided with a few examples before asking it to generate a response.
