from crewai import Crew
from agents.travel_agent import create_travel_agent
from agents.hotel_agent import create_hotel_agent
from agents.budget_agent import create_budget_agent
from tasks.travel_task import create_travel_task
from tasks.hotel_task import create_hotel_task
from tasks.budget_task import create_budget_task


def generate_travel_plan(user_query):

    query_lower = user_query.lower()

    # 🔹 Detect query type
    if "hotel" in query_lower:
        agent = create_hotel_agent()
        task = create_hotel_task(agent, user_query)

    elif "budget" in query_lower or "optimize" in query_lower:
        agent = create_budget_agent()
        task = create_budget_task(agent, user_query)

    else:
        agent = create_travel_agent()
        task = create_travel_task(agent, user_query)

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    result = crew.kickoff()
    return result.raw
