# models/ai_model.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_quiz(topic, difficulty, quiz_type):
    prompt = f"Generate a {difficulty} {quiz_type} quiz on the topic: {topic}."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful quiz generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response["choices"][0]["message"]["content"]
