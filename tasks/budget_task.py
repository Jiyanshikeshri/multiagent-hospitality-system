from crewai import Task

def create_budget_task(agent, context_text):
    return Task(
        description=f"""
        Based on the following travel plan and conversation:

        {context_text}

        Analyze total estimated cost.
        Suggest cost optimizations if exceeding budget.
        """,
        expected_output="Optimized budget analysis.",
        agent=agent
    )
