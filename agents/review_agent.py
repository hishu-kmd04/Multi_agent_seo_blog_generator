import deepseek

class ReviewAgent:
    def review_content(self, content):
        prompt = f"Proofread this blog post, fix grammar issues, and improve readability:\n{content}"
        response = deepseek.chat(prompt, model="deepseek-r1")
        return response["choices"][0]["text"]
