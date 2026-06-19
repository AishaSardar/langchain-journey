from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(system_prompt, user_message, temperature=0.7):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=temperature,
        max_tokens=1000
    )
    return response.choices[0].message.content

print("Day 3 — Prompt Engineering Techniques")
print("=" * 45)

# ─────────────────────────────────────────
# TECHNIQUE 1: Zero-shot prompting
# Ask directly with no examples
# ─────────────────────────────────────────
print("\n📌 TECHNIQUE 1: Zero-shot Prompting")
print("-" * 45)

zero_shot_system = "You are a helpful assistant."
zero_shot_query = "Classify this text as Positive, Negative or Neutral: 'The food was okay but the service was terrible.'"

result1 = ask(zero_shot_system, zero_shot_query)
print(f"Result: {result1}")

# ─────────────────────────────────────────
# TECHNIQUE 2: Few-shot prompting
# Give examples before asking
# ─────────────────────────────────────────
print("\n📌 TECHNIQUE 2: Few-shot Prompting")
print("-" * 45)

few_shot_system = """You are a sentiment classifier. 
Here are some examples:

Text: 'I love this product!' → Positive
Text: 'This is the worst experience ever.' → Negative
Text: 'The package arrived.' → Neutral
Text: 'Amazing quality, will buy again!' → Positive
Text: 'Not what I expected at all.' → Negative

Now classify the text the user gives you. 
Reply with ONLY one word: Positive, Negative, or Neutral."""

few_shot_query = "The food was okay but the service was terrible."

result2 = ask(few_shot_system, few_shot_query)
print(f"Result: {result2}")
print("\n👆 Compare result 1 vs result 2 — same question, very different output quality!")

# ─────────────────────────────────────────
# TECHNIQUE 3: Chain of Thought prompting
# Tell AI to think step by step
# ─────────────────────────────────────────
print("\n📌 TECHNIQUE 3: Chain of Thought Prompting")
print("-" * 45)

cot_system = """You are a math tutor.
When solving problems, always:
1. Read the problem carefully
2. Identify what is given
3. Write your step-by-step solution
4. State the final answer clearly"""

cot_query = """A shop sells apples for Rs 50 each and oranges for Rs 30 each. 
Ayesha buys 4 apples and 6 oranges. 
She pays with Rs 500. How much change does she get?"""

result3 = ask(cot_system, cot_query, temperature=0.3)
print(f"Result:\n{result3}")

# ─────────────────────────────────────────
# TECHNIQUE 4: Role prompting
# Give AI a specific expert identity
# ─────────────────────────────────────────
print("\n📌 TECHNIQUE 4: Role Prompting")
print("-" * 45)

# Same question asked to 3 different roles
question = "Should I learn Python or JavaScript first?"

roles = [
    ("AI Engineer", "You are a senior AI Engineer with 10 years experience. Give practical career advice."),
    ("University Professor", "You are a Computer Science professor. Give academic and theoretical perspective."),
    ("Freelancer", "You are a freelancer who earns money online through coding. Give practical income-focused advice."),
]

for role_name, role_system in roles:
    print(f"\n🎭 As a {role_name}:")
    result = ask(role_system, question, temperature=0.5)
    print(result)
    print("-" * 45)

# ─────────────────────────────────────────
# BONUS: Interactive prompt tester
# ─────────────────────────────────────────
print("\n📌 BONUS: Test Your Own Prompts")
print("-" * 45)
print("Now YOU write a system prompt and test it!")
print("Type 'quit' to exit\n")

custom_system = input("Enter your system prompt: ").strip()

while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() == "quit":
        break
    if not user_input:
        continue
    reply = ask(custom_system, user_input)
    print(f"\nAI: {reply}")