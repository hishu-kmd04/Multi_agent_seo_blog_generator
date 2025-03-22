import os

def save_blog(topic, outline, content, optimized_content):
    filename = f"blogs/{topic.replace(' ', '_')}.txt"
    os.makedirs("blogs", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Topic: {topic}\n\nOutline:\n{outline}\n\nContent:\n{content}\n\nOptimized Content:\n{optimized_content}")
    print(f"✅ Blog saved to {filename}")
