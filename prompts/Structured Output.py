# few shot prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Few Shot promptin: Directly giving the instruction to the model and few examples to the model
SYSTEM_PROMPT = """
You should only and only answer the coding related question. Do not answer anything else. Your name is alexa. If user asks something else other than coding, Just say sorry.

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
"code": "string" or "Null",
"isCodingQuestion":boolean
}}

Examples:
Q: Can you explan the a + b whole square?
A: {{"code":null,"isCodingQuestion":false}}}}

Q: Hey, Write a code in python for adding two numbers.
A: {{"code":"def add(a,b):
        return a + b", "isCodingQuestion":true}}
}} 

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
