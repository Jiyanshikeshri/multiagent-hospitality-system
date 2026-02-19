from crewai import Task

def create_hotel_task(agent, context_text):
    return Task(
        description=f"""
        Based on the following conversation context:

        {context_text}

        Suggest 3 well-rated hotels near the destination discussed.

        Include:
        - Hotel Name
        - Approx price per night
        - Key amenities
        - Why suitable
        """,
        expected_output="3 suitable hotels.",
        agent=agent
    )
