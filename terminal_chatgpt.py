import subprocess
import sys

try:
    import openai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])

import openai
# 'pip install pandas openai' this is necessary to avoid error: ModuleNotFoundError: No module named 'openai'
import re
import time

openai.api_key = "CHANGEME"

def ask_gpt(prompt, model, max_tokens):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.5,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    message = response.choices[0].text.strip()
    return message

print("Hi, I'm ChatGPT! What would you like to talk about today?")
model = "text-davinci-002"
max_tokens = 2049
while True:
    user_input = input("> ")
    prompt = f"You: {user_input}\nChatGPT:"
    response = ""
    for i in range(0, len(prompt), max_tokens):
        response += ask_gpt(prompt[i:i+max_tokens], model, max_tokens)
    print(response)
