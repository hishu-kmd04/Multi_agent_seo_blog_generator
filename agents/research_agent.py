import json
import requests

class ResearchAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_trending_topics(self):
        prompt = "Give me 5 trending HR topics and relevant information for 2025."

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "deepseek/deepseek-r1:free",
                "messages": [{"role": "user", "content": prompt}]
            })
        )

        if response.status_code == 200:
            result = response.json()
            return [choice["message"]["content"] for choice in result.get("choices", [])]
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            return None
