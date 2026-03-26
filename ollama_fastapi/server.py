from fastapi import FastAPI, Body, HTTPException
from ollama import _client, Client

app = FastAPI()
client = Client(
    host="http://localhost:11434",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contact-us")
def read_root():
    return {"email": "World"}

@app.post("/chat")
def chat(message: str = Body(..., description="Message")):
    response = client.chat(model="yi-coder:1.5b", messages=[
        {"role":"user", "content":message}
    ])

    return {"response":response.message.content}

