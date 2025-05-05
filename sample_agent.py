# -*- coding: utf-8 -*-
"""
Created on Tue May  6 00:02:44 2025

@author: HP
"""
from dotenv import load_dotenv
import os
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
import requests

#AI agent means a piece of code which have access of tools to complete a task/based on user query thats it 
#and if you give them an autonomy for planning and action its agentic AI .Simple 

#AI agent +Tools +Autonomy for actionand planning = Agentic AI 

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")




# === Tool 1: Search Wikipedia for capital ===
def get_capital_of_country(country: str) -> str:
    response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    if response.status_code == 200:
        data = response.json()
        return data[0]['capital'][0]
    return "Unknown"

# === Tool 2: Get weather using OpenWeatherMap API (or mock) ===
def get_weather(city: str) -> str:
    # Replace with real API if needed
    return f"The weather in {city} is currently sunny and 25°C."

# Wrap functions as LangChain tools
tools = [
    Tool(
        name="CapitalFinder",
        func=lambda x: get_capital_of_country(x),
        description="Use this to find the capital city of a country"
    ),
    Tool(
        name="WeatherFetcher",
        func=lambda x: get_weather(x),
        description="Use this to get the current weather of a city"
    ),
]

# Initialize the agent with tools
llm = ChatOpenAI(temperature=0)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent on a compound task
query = "What is the capital of France, and what is the weather like there right now?"
result = agent.run(query)
print("\nFinal Answer:", result)
