from crewai import Agent
from config.llm_config import get_llm

def create_travel_agent():
    return Agent(
        role="Travel Planner",
        goal="Create a detailed and well-structured travel itinerary.",
        backstory="An expert travel planner specializing in domestic tourism.",
        verbose=True,
        llm=get_llm()
    )
