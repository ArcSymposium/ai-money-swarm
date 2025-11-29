from crewai import Agent, Task, Crew
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:3b", temperature=0.8)

# === THE 10 MONEY-MAKING SUB-AGENTS (2025 proven) ===
agents = [
    Agent(role="YouTube → Newsletter SaaS Builder",          goal="Create a $29/mo YouTube summary product", backstory="Specialist in viral content tools", llm=llm),
    Agent(role="Cold Email Copywriter",                     goal="Write 10 cold emails that get 8–15 % reply rates", backstory="Trained on $400 k+ of winning campaigns", llm=llm),
    Agent(role="Local Lead-Gen Site Flipper",               goal="Build SEO-optimized lead sites for roofers/pools/lawns", backstory="Has sold 47 sites in 2024–2025", llm=llm),
    Agent(role="AI Content Agency Owner",                   goal="Generate 30 blog posts/month for clients at $300 each", backstory="Runs a 6-figure agency with zero writers", llm=llm),
    Agent(role="Twitter/X Growth Hacker",                goal="Grow niche accounts to 10 k followers and sell sponsorships", backstory="Grew 9 accounts past monetization", llm=llm),
    Agent(role="OnlyFans / Fanvue Manager",                 goal="Fully automate messaging + content calendar for models", backstory="Manages 11 creators profitably", llm=llm),
    Agent(role="Airbnb Pricing & Messaging Bot",            goal="Maximize nightly rates + auto-reply to inquiries", backstory="Increased one host’s revenue 41 %", llm=llm),
    Agent(role="Etsy Digital Product Creator",              goal="Design and list print-on-demand planners, trackers, art", backstory="Makes $7 k–$18 k/mo passive", llm=llm),
    Agent(role="Stripe SaaS Boilerplate Generator",         goal="Spin up paid SaaS in <10 min with login, billing, dashboard", backstory="Sold 83 licenses at $499", llm=llm),
    Agent(role="Master Orchestrator",                       goal="Coordinate the other 9 agents, track revenue, reinvest profits", backstory="CEO of this swarm", llm=llm, allow_delegation=True)
]

tasks = [
    Task(
        description=f"""
        Activate ALL 10 agents simultaneously.
        Each agent must produce one complete, ready-to-sell or ready-to-launch income stream today.
        The Master Orchestrator will assign priorities, track output, and create a revenue dashboard.
        Save every artifact (code, copy, sites, listings) into dated folders.
        End with a one-page report: "Today's projected monthly recurring revenue from this swarm".
        """,
        expected_output="10 folders + revenue_report.md",
        agent=agents[9]  # Master Orchestrator gets the big task
    )
]

crew = Crew(agents=agents, tasks=tasks, verbose=2)
result = crew.kickoff()

print("\nSWARM COMPLETE — CHECK ~/my-agents/ FOR 10 READY-TO-MONETIZE PROJECTS\n")
print(result)
