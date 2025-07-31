from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import phi.api
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
import phi
from phi.playground import Playground, serve_playground_app
phi.api=os.getenv("PHI_API_KEY")


#web search agent
web_search_agent=Agent(
    name='Web Search Agent',
    role="search the web for the information",
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

#financial agent
finance_agent=Agent(
    name='Financial Agent',
    model=Groq(id="llama-3.2-90b-vision-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

app=Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("playground:app", reload=True)