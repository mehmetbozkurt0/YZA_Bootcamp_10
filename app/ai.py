import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"

def get_ai_suggestions(task_summary: dict) -> str:
    completed = task_summary["completed"]
    not_completed = task_summary["not_completed"]

    prompt = (
        f"Son günlerde tamamladığım görevler: {', '.join(completed) if completed else 'yok'}.\n"
        f"Tamamlayamadığım görevler: {', '.join(not_completed) if not_completed else 'yok'}.\n"
        "Bunlara göre bana yarın için kısa ve motive edici bir öneri ver. Kişisel gelişim odaklı olabilir."
    )


    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text'].strip()
        else:
            print("Gemini API hatası:", response.status_code, response.text)
            return "AI önerisi alınamadı!"
    except Exception as e:
        print("AI istek hatası:", e)
        return "AI önerisi alınamadı!"
