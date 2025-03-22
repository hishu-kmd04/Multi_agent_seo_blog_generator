# 🚀 Multi-Agent SEO Blog Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📌 Overview
The **Multi-Agent SEO Blog Generator** automates the process of researching, planning, generating, and optimizing blog content. It utilizes AI-driven agents to create high-quality, SEO-friendly articles effortlessly.

## 🛠️ Key Features
✅ **Automated Blog Writing** – Generates structured, well-written articles.  
✅ **Trending Topic Research** – Fetches the latest topics dynamically.  
✅ **SEO Optimization** – Enhances content for search engine visibility.  
✅ **Markdown Export** – Saves the final blog as a Markdown file.

## 🧠 How It Works
The system follows a multi-agent approach, where each AI agent plays a specialized role:

🔍 **Research Agent** – Identifies trending topics.  
📝 **Content Planning Agent** – Creates an article outline.  
✍️ **Content Generation Agent** – Writes engaging blog content.  
📈 **SEO Optimization Agent** – Refines content for search ranking.

## 🏗️ Project Structure
```
📂 multi_agent_seo_blog_generator
│── 📂 agents
│   ├── research_agent.py
│   ├── content_planning_agent.py
│   ├── content_generation_agent.py
│   ├── seo_optimization_agent.py
│── 📂 utils
│   ├── save_blog.py
│── .env
│── blog_post.md
│── main.py
│── requirements.txt
│── README.md
```

## 🚀 Getting Started
### 1️⃣ Prerequisites
Ensure you have **Python 3.8+** installed and set up your environment:
```sh
pip install -r requirements.txt
```

### 2️⃣ Setup Environment Variables
Create a `.env` file and add your API key:
```
OPENROUTER_API_KEY=your_api_key_here
```

### 3️⃣ Run the Project
Execute the script to generate a blog post:
```sh
python main.py
```

## 📂 Output
The generated blog content will be saved as `blog_post.md`.

## 🎯 Future Improvements
- 🏗️ Add more advanced SEO techniques.
- 🌐 Integrate multilingual support.
- 📊 Improve content quality with additional NLP models.

## 📜 License
This project is licensed under the **MIT License**.

💡 *Contributions are welcome! Feel free to fork and improve the project.*

