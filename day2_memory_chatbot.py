from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# This list holds the FULL conversation history
conversation_history = []

# System prompt — this gives the AI its personality
SYSTEM_PROMPT = """You are Aria, a friendly and smart AI assistant. 
You remember everything said in the conversation.
You speak in a warm, encouraging tone.
When you don't know something, you say so honestly."""

def chat(user_message):
    # Step 1 — add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Step 2 — send system prompt + full history to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT}
        ] + conversation_history,
        temperature=0.7,
        max_tokens=1000
    )
    
    # Step 3 — get the AI reply
    ai_reply = response.choices[0].message.content
    
    # Step 4 — add AI reply to history too
    conversation_history.append({
        "role": "assistant",
        "content": ai_reply
    })
    
    return ai_reply

def show_history():
    print("\n--- Conversation History ---")
    for i, message in enumerate(conversation_history):
        role = "You" if message["role"] == "user" else "Aria"
        print(f"{i+1}. {role}: {message['content'][:100]}...")
    print("----------------------------\n")


print("=" * 50)
print("   Aria — AI Chatbot with Memory")
print("   Commands: 'quit' | 'history' | 'clear'")
print("=" * 50)
print()

while True:
    user_input = input("You: ").strip()
    
    if not user_input:
        continue
    
    if user_input.lower() == "quit":
        print("Aria: Goodbye! See you next time 👋")
        break
    
    elif user_input.lower() == "history":
        show_history()
        continue
    
    elif user_input.lower() == "clear":
        conversation_history.clear()
        print("Aria: Memory cleared! Starting fresh.\n")
        continue
    
    reply = chat(user_input)
    print(f"\nAria: {reply}\n")