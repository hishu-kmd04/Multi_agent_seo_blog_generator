import os
import json
import requests
from dotenv import load_dotenv
from agents.research_agent import ResearchAgent
from agents.content_planning_agent import ContentPlanningAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.seo_optimization_agent import SEOOptimizationAgent

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("❌ Error: API key is missing. Check your .env file.")

# Initialize agents
research_agent = ResearchAgent(api_key)
content_planner = ContentPlanningAgent(api_key)
content_generator = ContentGenerationAgent(api_key)
seo_optimizer = SEOOptimizationAgent(api_key)

# Fetch trending topics
try:
    trending_topics = research_agent.get_trending_topics()
    chosen_topic = trending_topics[0] if trending_topics else "Latest AI Trends"
    print(f"✅ Chosen Topic: {chosen_topic}")
except Exception as e:
    print(f"❌ Error fetching trending topics: {e}")
    chosen_topic = "Latest AI Trends"

# Generate blog outline
outline = None
try:
    outline = content_planner.generate_outline(chosen_topic)
    if not outline:
        print("⚠️ Failed to generate blog outline. Skipping content generation.")
except Exception as e:
    print(f"❌ Error in content planning: {e}")

# Generate content
blog_content = None
if outline:
    try:
        blog_content = content_generator.generate_content(outline)
        if not blog_content:
            print("⚠️ Failed to generate blog content. Skipping SEO optimization.")
    except Exception as e:
        print(f"❌ Error in content generation: {e}")

# Optimize for SEO
optimized_content = None
if blog_content:
    try:
        optimized_content = seo_optimizer.optimize_for_seo(blog_content)
        if not optimized_content:
            print("⚠️ SEO Optimization failed.")
    except Exception as e:
        print(f"❌ Error in SEO Optimization: {e}")

# Save the blog post as Markdown
def save_as_markdown(content, filename="blog_post.md"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

if optimized_content:
    save_as_markdown(optimized_content)
    print("✅ Blog post saved in Markdown format.")

print("\n✅ Process completed.")
