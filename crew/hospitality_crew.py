from crewai import Crew
from agents.travel_agent import create_travel_agent
from agents.hotel_agent import create_hotel_agent
from agents.budget_agent import create_budget_agent
from tasks.travel_task import create_travel_task
from tasks.hotel_task import create_hotel_task
from tasks.budget_task import create_budget_task


def run_crew(user_query):

    # Create agents
    travel_agent = create_travel_agent()
    hotel_agent = create_hotel_agent()
    budget_agent = create_budget_agent()

    # Step 1: Travel Task
    travel_task = create_travel_task(travel_agent, user_query)

    # Step 2: Hotel Task depends on travel output
    hotel_task = create_hotel_task(hotel_agent, travel_task)

    # Step 3: Budget Validation depends on both
    budget_task = create_budget_task(budget_agent, travel_task, hotel_task)

    crew = Crew(
        agents=[travel_agent, hotel_agent, budget_agent],
        tasks=[travel_task, hotel_task, budget_task],
        verbose=True
    )

    result = crew.kickoff()

    # Combine outputs
    final_output = ""
    for task_output in result.tasks_output:
        final_output += task_output.raw + "\n\n"

    result.raw = final_output
    return result
