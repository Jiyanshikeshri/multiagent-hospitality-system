from crewai import Task

def create_travel_task(agent, user_query):
    return Task(
        description=f"""
        Create a detailed travel itinerary based on the following request:
        {user_query}
        
        Include:
        - Day-wise plan
        - Activities
        - Food suggestions
        - Time breakdown
        """,
        agent=agent,
        expected_output="A complete day-wise travel itinerary."
    )
