from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    verbose=True,
)

result = crew.kickoff(
    inputs={
        "topic": "Web Development Complete RoadMap | from Basics to Advanced"
    }
)

print(result)
