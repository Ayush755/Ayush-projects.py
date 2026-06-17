import os
import requests
import json

API_KEY = os.getenv("API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

print("Hii Ayush🗿, Twinny 👾 this side....Tell me what you want to know...huh!?\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["chup ho ja", "quit"]:
        break

    payload = {
        "contents": [{"parts": [{"text": user_input}]}]
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(URL, headers=headers, json=payload)
        data = response.json()
        ai_response = data['candidates'][0]['content']['parts'][0]['text']
        print(f"\nTwinny Ai👾 : {ai_response}\n")
    except Exception as e:
        print(f"Error: {e}")
