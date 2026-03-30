# Chain of Thought shot prompting
from dotenv import load_dotenv
from openai import OpenAI


import json

load_dotenv()

client = OpenAI()

# Few Shot promptin: Directly giving the instruction to the model and few examples to the model
SYSTEM_PROMPT = """
    You're an expoert AI Assistant in resolving user queries using chain of thought.
    You work on Start, Plan and Output steps.
    You need to first Plan what needs to be done. The Plan can be multiple steps.
    Once you think enough plan has been done, finally you can give an output.
    
    Rules:
    -   Strictly Follow the given JSON output format
    -   Only run on step at a time.
    - The sequence of steps is start (where user gives an input), Plan(that can be multiple times) and finally output (which is going to be displayed to the user).
    
    Output JSON Format:
    {
    "Step":"Start" | "Plan" | "Output", "content":"string"
    }
    
    Example:
    Start: Hey, can you solve 2 + 3 * 5 /10
    Plan: {
            "step":"Plan":"content":"Seems like user is interested in math problem"
            }
    Plan:{
            "step":"Plan":"content":"Looking at the problem, we should solve this using BODMAS method"
    }
    Plan:{
        "step":"Plan":"content":"Yes, The BODMAS is correct thing to be done here."
    }
    Plan:{
        "step":"Plan":"content":"First we must multiply 3 * 5 which is 15"
    }
    }
    Plan:{
        "step":"Plan":"content":"Now the new equation is 2 _+ 15 / 10"
    }
    }
    Plan:{
        "step":"Plan":"content":"We must perform divide that is 15/10 = 1.5"
    }
    }
    Plan:{
        "step":"Plan":"content":"Now the new equation is 2 + 1.5"
    }
    }
    Plan:{
        "step":"Plan":"content":"Now Finally lets perform the add"
    }
    }
    Plan:{
        "step":"Plan":"content":"Great, we have solved and finally left with 3.5 as ans"
    }
    }
    Output:{
        "step":"Output":"content":"3.5"
    }
"""

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

print("\n\n\n")

user_query = input("")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=message_history
    )
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "Start":
        print("Starting LLM Loop", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "Plan":
        print("Thinking", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "Output":
        print("Result", parsed_result.get("content"))
        break

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": "Hey There, My name is Sunny. Who are you"}
#     ]
# )

# print(response.choices[0].message.content)

# 1.Few shot Prompting: The model is provided with a few examples before asking it to generate a response.
