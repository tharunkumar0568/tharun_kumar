import requests
import json

API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

while True:
    msg = input("You: ")

    if msg.lower() == "bye":
        print("AI: Bye! Have a great day!")
        break

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": msg}
        ]
    }

    r = requests.post(URL, headers=headers, json=payload)
    result = r.json()

    print("AI:", result["choices"][0]["message"]["content"])
