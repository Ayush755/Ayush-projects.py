import requests
import os
from config
import base64
import VISION_API_KEY

API_KEY = os.getenv("API_KEY")

# Read image
with open("/storage/emulated/0/Download/Ai vision/image.jpg", "rb") as f:
    image = base64.b64encode(f.read()).decode("utf-8")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5->

headers = {
    "Content-Type": "application/json"
}

payload = {
    "contents": [
        {
            "parts": [
                {"text": "describe the image"},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": image
                    }
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)

print(response.json()["candidates"][0]["content"]["parts"][0]["text"])
