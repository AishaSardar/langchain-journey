from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat(user_message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a Python tutor who explains things simply."},
            {"role": "user", "content": user_message}
        ],
        temperature=1.0,
        max_tokens=500
    )
    return response.choices[0].message.content

print("CLI Chatbot (Groq + LLaMA 3) — type 'quit' to exit\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    reply = chat(user_input)
    print(f"AI: {reply}\n")