# 🤖 AI Blog Crew

An AI-powered technical blog generation system built using **CrewAI**, **Google Gemini**, and **Tavily Search**.

This project uses multiple AI agents to research a given topic and generate a detailed, professional technical blog in Markdown format.

## 🚀 Project Overview

The project automates the process of creating technical blogs using a multi-agent AI workflow.

It consists of two specialized AI agents:

- 🔍 **AI Researcher** — Researches the given topic and collects relevant information.
- ✍️ **Technical Blog Writer** — Uses the research to create a professional technical blog.

The agents work together sequentially to produce the final blog.

## ✨ Features

- 🤖 Multi-Agent AI System
- 🔍 Automated Web Research
- ✍️ AI-powered Technical Blog Writing
- 🌐 Tavily Search Integration
- 🧠 Google Gemini LLM
- 🔄 Sequential Agent Workflow
- 💾 Agent Memory
- 📝 Markdown Blog Generation
- ⚡ Automated End-to-End Blog Creation

## 🧠 AI Agents

### 🔍 1. AI Researcher

**Role:** AI Researcher

**Goal:** Research the given topic and collect important information and insights.

**Expertise:**
- Artificial Intelligence
- Data Science
- Generative AI

The researcher uses the Tavily Search Tool to gather relevant information from the web.

### ✍️ 2. Technical Blog Writer

**Role:** Technical Blog Writer

**Goal:** Write a detailed and professional technical blog based on the research.

The writer converts the research findings into a structured Markdown blog post.

## 🔄 Workflow

The project follows a sequential workflow:

```text
          📌 Topic
             ↓
      🔍 AI Researcher
             ↓
       🌐 Web Search
        (Tavily)
             ↓
      📚 Research Report
             ↓
    ✍️ Technical Blog Writer
             ↓
       📝 Final Blog
             ↓
     new-blog-post.md

🛠️ Technologies Used

🐍 Python

🤖 CrewAI

🧠 Google Gemini

🌐 Tavily Search

🔐 Python-dotenv

📝 Markdown


📂 Project Structure

AI-Blog-Crew/
│
├── agents.py
├── tasks.py
├── tools.py
├── Crew.py
├── new-blog-post.md
├── .env
└── README.md

⚙️ How It Works

Step 1 — Topic Input

A topic is provided to the Crew through the kickoff() method.

Example:

inputs={
    "topic": "Web Development Complete RoadMap | from Basics to Advanced"
}

Step 2 — Research

The AI Researcher receives the topic and performs research using the Tavily Search Tool.

It generates a detailed research report containing relevant information and key insights.

Step 3 — Blog Writing

The Technical Blog Writer uses the research and creates a professional technical blog in Markdown format.

Step 4 — Output

The generated blog is automatically saved as:

new-blog-post.md

🔑 Environment Variables

Create a .env file in the project directory and add your API keys:

GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key

⚠️ Never upload your API keys or .env file to GitHub.

Add .env to your .gitignore file:

.env

📦 Installation

Clone the repository:

git clone https://github.com/your-username/your-repository-name.git

Navigate to the project directory:

cd your-repository-name

Install the required packages:

pip install crewai crewai-tools python-dotenv

▶️ Run the Project

After configuring your API keys, run:

python Crew.py

The CrewAI agents will execute sequentially and generate the final blog.

The generated blog will be saved in:

new-blog-post.md

💡 Example Topic

The current project uses:

Web Development Complete RoadMap | from Basics to Advanced

The system researches the topic and generates a complete technical blog based on the collected information.

🎯 Objective

The main objective of this project is to demonstrate how multi-agent AI systems can automate technical content creation by dividing the work between specialized AI agents.

🔮 Future Improvements

📚 Support multiple blog topics through user input

🌐 Add a web-based interface

📄 Generate blogs in multiple formats

🎨 Improve blog formatting and structure

🔍 Add more specialized research agents

🚀 Deploy the application for public use


👨‍💻 Author

Anirudh Gupta

🎓 B.Tech — Computer Science & Engineering (Data Science)

📍 Lucknow, Uttar Pradesh, India


---

🤖 Built with CrewAI, Google Gemini & Tavily
