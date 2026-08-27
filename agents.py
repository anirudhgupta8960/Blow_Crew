from crewai import Agent, LLM
from tools import search_tool

from dotenv import  load_dotenv
import os

load_dotenv()

llm = LLM(
    model="gemini/gemini-3.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

blog_researcher = Agent(
    role="AI Researcher",
    goal="Research the topic {topic}",
    backstory="Expert in AI, Data Science and Generative AI.",
    verbose=True,
    memory=True,
    llm=llm,
    tools=[search_tool],
    allow_delegation=True,
)

blog_writer = Agent(
    role="Technical Blog Writer",
    goal="Write a detailed blog on {topic}",
    backstory="Expert technical content writer.",
    verbose=True,
    memory=True,
    llm=llm,
    tools=[search_tool],
    allow_delegation=False,
)