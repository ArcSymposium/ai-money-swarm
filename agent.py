from crewai import Agent, Task, Crew
from langchain_ollama import ChatOllama

# Your private brain — 100 % local, no internet needed after this
llm = ChatOllama(model="llama3.2:3b", temperature=0.7)

# This single agent can build anything you ask for
builder = Agent(
    role="Autonomous Full-Stack AI Engineer",
    goal="Turn any plain-English request into working code, agents, APIs, or complete apps",
    backstory="You are running entirely on a Chromebook with zero cloud dependencies",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Change this text to whatever you want built — examples below
task = Task(
    description="""
    Build a complete, ready-to-run YouTube video → Newsletter SaaS newsletter generator with these exact features:
    1. User pastes any YouTube URL
    2. Automatically fetches the transcript
    3. Creates a beautiful newsletter in Markdown with title, key points, quotes, and call-to-action
    4. Saves it as newsletter.md in the current folder
    5. Also prints the full newsletter to the screen
    Make sure the code works with zero extra installs beyond what I already have.
    """,
    expected_output="A working Python script that does all of the above",
    agent=builder
)

crew = Crew(agents=[builder], tasks=[task], verbose=2)
result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)
