from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")

web_agent=Agent(
    name="Web_agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the source",
    show_tool_calls=True,
    markdown=True
)

finance_agent=Agent(
    name="Finance Agent",
    role="Get financial Data from trusted source",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_info=True)],
    instructions="Use tables to display data in structured way",
    show_tool_calls=True,
    markdown=True
)

agent_team=Agent(
    team=[web_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["lways include the source","Use tables to display data in structured way"],
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("Analyze between NVIDIA, Meta, Google from these which stock should i buy now")
