from crewai import Task
from agents import blog_researcher, blog_writer

research_task = Task(
    description="""
    Research the topic:
    {topic}
    
    Collect the latest information and key insights.
    """,
    expected_output="Detailed research report.",
    agent=blog_researcher,
)

write_task = Task(
    description="""
    Using the research, write a professional blog on:
    {topic}
    """,
    expected_output="A complete technical blog in Markdown.",
    agent=blog_writer,
    output_file="new-blog-post.md",
)