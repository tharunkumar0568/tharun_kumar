from flask import Flask, request, jsonify, render_template
import requests
import re

app = Flask(__name__)

API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# ✅ Allowed topic keywords
CASUAL_KEYWORDS = [
    "hi", "hello", "how are you", "your name", "who are you",
    "good morning", "good evening", "bye"
]

JAVA_KEYWORDS = [
    "java", "jdk", "jre", "jvm",
    "class", "object", "method", "constructor",
    "inheritance", "polymorphism", "abstraction", "encapsulation",
    "interface", "extends", "implements",
    "exception", "try", "catch", "finally",
    "array", "string", "loop", "for", "while",
    "spring", "hibernate"
]

def is_allowed(message: str) -> bool:
    msg = message.lower()

    for word in CASUAL_KEYWORDS + JAVA_KEYWORDS:
        if word in msg:
            return True
    return False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")

    # ❌ Restriction check
    if not is_allowed(user_msg):
        return jsonify({
            "reply": "❌ Sorry! I can only answer casual chat or SQL-related questions."
        })

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are a friendly assistant that ONLY answers casual conversation and java-related questions."
            },
            {
                "role": "user",
                "content": user_msg
            }
        ]
    }

    try:
        r = requests.post(URL, headers=HEADERS, json=payload, timeout=20)
        r.raise_for_status()
        data = r.json()
        reply = data["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)