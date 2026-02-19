from crewai import Crew
from agents.hotel_agent import create_hotel_agent
from tasks.hotel_task import create_hotel_task

def generate_hotels(itinerary_text):

    #  Create agent instance
    hotel_agent = create_hotel_agent()

    #  Pass correct object
    hotel_task = create_hotel_task(hotel_agent, itinerary_text)

    crew = Crew(
        agents=[hotel_agent],
        tasks=[hotel_task],
        verbose=True
    )

    result = crew.kickoff()
    return result.raw

