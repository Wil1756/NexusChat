from openai import OpenAI
from src.prompt import system_instruction

client = OpenAI()

messages = [
    {"role": "system", "content": system_instruction}
]
def get_response(messages, model="gpt-4o-mini", temperature= 0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content
