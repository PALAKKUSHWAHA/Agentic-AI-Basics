creted a folder called parent_folder then inside this Activate Virtual Environment  ".venv " file ... cmd:python -m venv .venv
open .venv new terminal and run :pip install google-adk(sucessfully installing ADK)
create the following project structure:


parent_folder/
    multi_tool_agent/
        __init__.py
        agent.py
        .env

Get an API key from Google AI Studio. and inside .env paste API key.....

what this agent.py file will do:it will creates an AI agent named "weather_time_agent".

tells it to use the "gemini-2.0-flash" model (a Google LLM).

Gives it:

A description (“I help with time and weather questions”).

Instructions (“Be helpful and answer based on weather/time tools”).

A list of tools (get_weather, get_current_time) that it can use to respond to user queries.
