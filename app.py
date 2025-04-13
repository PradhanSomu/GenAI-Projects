# This example shows how to create a team of agents that can search the web for financial news and analyze it using the DuckDuckGo and YFinance tools.
# It uses the agno library to create agents, tools, and a team, and stores the data in a PostgreSQL database.
# Import the necessary libraries
from agno.agent import Agent
from agno.memory.v2 import Memory
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.postgres import PostgresStorage
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up the database connection URL
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
memory_db = PostgresMemoryDb(table_name="memory", db_url=db_url)
memory = Memory(db=memory_db)

# Create the agents and team
# The web agent searches the web for information using DuckDuckGo
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    agent_id="web_agent",
    instructions=[
        "You are an experienced web researcher and news analyst! 🔍",
    ],
    memory=memory,
    enable_user_memories=True,
    show_tool_calls=True,
    markdown=True,
    storage=PostgresStorage(
        table_name="web_agent", db_url=db_url, auto_upgrade_schema=True
    ),
)

# The finance agent retrieves financial data using YFinance
# It provides stock prices, analyst recommendations, and company information
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    agent_id="finance_agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)
    ],
    instructions=[
        "You are a skilled financial analyst with expertise in market data!",
        "Follow these steps when analyzing financial data:",
        "Start with the latest stock price, trading volume, and daily range",
        "Present detailed analyst recommendations and consensus target prices",
        "Include key metrics: P/E ratio, market cap, 52-week range",
        "Analyze trading patterns and volume trends",
    ],
    memory=memory,
    enable_user_memories=True,
    show_tool_calls=True,
    markdown=True,
)

# Create a team of agents that can work together to analyze financial news
Financial_team = Team(
    name="Financial News Team",
    description="A team of agents that search the web for financial news and analyze it.",
    members=[
        web_agent,
        finance_agent,
    ],
    model=OpenAIChat(id="gpt-4o"),
    mode="route",
    team_id="financial_news_team",
    instructions=[
        "You are the lead editor of a prestigious financial news desk! 📰",
        "Use USD as currency.",
        "If the user is just being conversational, you should respond directly WITHOUT forwarding a task to a member.",
    ],
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    show_members_responses=True,
    storage=PostgresStorage(
        table_name="financial_news_team",
        db_url=db_url,
        mode="team",
        auto_upgrade_schema=True,
    ),
    memory=memory,
    enable_user_memories=True,
    expected_output="A good financial news report.",
)

# Create the playground app with the team and agents
# This app allows users to interact with the agents and team through a web interface
app = Playground(
    teams=[Financial_team],
    agents=[web_agent, finance_agent],
).get_app()

# Run the app
# This function serves the app using the agno library's built-in server
if __name__ == "__main__":
    serve_playground_app("app:app", reload=True)