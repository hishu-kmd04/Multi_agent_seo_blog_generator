import json
import requests

class ContentGenerationAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_content(self, outline):
        prompt = f"Write a detailed blog (2000 words) following this outline:\n{outline}"

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
            return result["choices"][0]["message"]["content"]
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            return None
