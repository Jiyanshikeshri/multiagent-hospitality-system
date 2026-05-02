from crewai import Crew
from agents.budget_agent import create_budget_agent
from tasks.budget_task import create_budget_task

def validate_budget(full_plan_text):

    # Create agent instance
    budget_agent = create_budget_agent()

    # Pass correct object
    budget_task = create_budget_task(budget_agent, full_plan_text)

    crew = Crew(
        agents=[budget_agent],
        tasks=[budget_task],
        verbose=True
    )

    result = crew.kickoff()
    return result.raw
