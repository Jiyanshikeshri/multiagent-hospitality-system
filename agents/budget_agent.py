from crewai import Agent
from config.llm_config import get_llm

def create_budget_agent():
    return Agent(
        role="Budget Optimization Specialist",
        goal="Ensure the complete travel plan stays within the specified budget and adjust if necessary.",
        backstory="An expert financial travel planner who ensures affordability without compromising experience.",
        verbose=True,
        llm=get_llm()
    )
