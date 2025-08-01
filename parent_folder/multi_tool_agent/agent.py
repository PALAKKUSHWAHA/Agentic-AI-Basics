# Import the datetime module to work with date and time functions
import datetime 

# Import ZoneInfo class from zoneinfo to handle timezone-aware datetime
from zoneinfo import ZoneInfo  

# Import Agent class from google.adk.agents to create and manage AI agents
from google.adk.agents import Agent  


# Define a tool function named `get_weather` that accepts a city name and returns weather data
def get_weather(city: str) -> dict:
    """
    Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """

    # Convert city name to lowercase and check if it is "new york"
    if city.lower() == "new york":
        # Return a mock success weather report if the city is New York
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        # Return an error if the city is not recognized
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


# Define a tool function named `get_current_time` that provides the current time in a given city
def get_current_time(city: str) -> dict:
    """
    Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    # Check if the provided city is "new york"
    if city.lower() == "new york":
        # Set the timezone string for New York
        tz_identifier = "America/New_York"
    else:
        # Return an error if the city is not supported
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    # Create a ZoneInfo object using the timezone identifier
    tz = ZoneInfo(tz_identifier)

    # Get the current datetime in the given timezone
    now = datetime.datetime.now(tz)

    # Format the current time into a readable string
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )

    # Return the formatted time as a success report
    return {"status": "success", "report": report}


# Create an Agent instance called `root_agent`
root_agent = Agent(
    # Set the name of the agent
    name="weather_time_agent",

    # Specify the LLM model the agent will use (in this case, Gemini 2.0 Flash)
    model="gemini-2.0-flash",

    # Describe the agent’s purpose
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),

    # Set the instructions the agent will follow while responding
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),

    # Register the tool functions (get_weather and get_current_time) that the agent can use
    tools=[get_weather, get_current_time],
)
