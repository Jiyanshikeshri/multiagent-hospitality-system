from crewai import Agent
from config.llm_config import get_llm

def create_hotel_agent():
    return Agent(
        role="Hotel Recommendation Specialist",
        goal="Suggest budget-friendly and well-rated hotels based on destination and budget constraints.",
        backstory="An expert hospitality consultant who specializes in recommending affordable and comfortable stays.",
        verbose=True,
        llm=get_llm()
    )
