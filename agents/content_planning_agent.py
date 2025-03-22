import json
import requests

class ContentPlanningAgent:
    def __init__(self, api_key: str, model: str = "deepseek/deepseek-r1:free"):
        self.api_key = api_key
        self.model = model
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"

    def generate_outline(self, topic: str) -> str | None:
        """Generates a detailed blog outline for a given topic."""
        prompt = f"Create a detailed blog outline for a 2000-word SEO-optimized article on '{topic}'."

        try:
            response = requests.post(
                url=self.api_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}]
                }),
                timeout=10  # Prevents hanging requests
            )

            response.raise_for_status()  # Raise HTTP errors (4xx, 5xx)

            result = response.json()
            print("🔍 API Response:", json.dumps(result, indent=2))  # Debugging step

            # Check if 'choices' exists in response
            choices = result.get("choices")
            if choices and isinstance(choices, list) and "message" in choices[0]:
                return choices[0]["message"].get("content", "No content found.")
            else:
                print("⚠️ Unexpected API response format:", result)
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ API Request Failed: {e}")
            return None
