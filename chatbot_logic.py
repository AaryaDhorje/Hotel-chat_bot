import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def get_bot_response(user_input):
    keywords = ["name of the hotel", "your hotel name", "what hotel is this", "what's the name of this hotel"]
    if any(kw in user_input.lower() for kw in keywords):
        return "Our hotel is called **The Serenity Bay Resort**. We're glad to have you here!"

    prompt = f"""
You are a helpful assistant for 'The Serenity Bay Resort'.
Answer questions clearly and politely based on common hotel policies.

Guest: {user_input}
Hotel Bot:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.5
    )

    return response.choices[0].message.content.strip()
