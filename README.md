# Agentic Financial News Analyzer with Agno and GPT-4o

An intelligent, multi-agent system that retrieves and analyzes real-time financial news using advanced LLMs and purpose-built tools. Built with the [Agno](https://github.com/agnos-ai/agno) framework and OpenAI’s GPT-4o, this project demonstrates a powerful application of agentic workflows for financial analysis.

## Features

- **Multi-Agent Architecture**  
  Two specialized agents — a Web Agent and a Finance Agent — work collaboratively within a team.

- **Real-Time Web Search**  
  The Web Agent uses DuckDuckGo to retrieve the latest financial news and updates.

- **Market Data Analysis**  
  The Finance Agent uses YFinance to provide stock prices, analyst recommendations, and key financial metrics.

- **Team-Based Reasoning**  
  Agents communicate via a centralized team controller with contextual memory and task routing.

- **PostgreSQL Integration**  
  Persistent memory and storage using a PostgreSQL backend for agents and team interactions.

- **Interactive Playground**  
  A web interface to interact with agents, ask queries, and get detailed financial insights.

## Tech Stack

- [Agno](https://github.com/agnos-ai/agno)
- [OpenAI GPT-4o](https://platform.openai.com/)
- [DuckDuckGo Tools (Agno)](https://docs.agnos.ai/tools/duckduckgo)
- [YFinance Tools (Agno)](https://docs.agnos.ai/tools/yfinance)
- PostgreSQL
- Python
- FastAPI (via Agno Playground)

## Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/financial-news-analyzer.git
cd financial-news-analyzer
```

### 2. Install Dependencies

```pip install -r requirements.txt
```

### 3. Set Up Environment Variables

```Create a .env file in the root directory and add your environment variables (e.g., OpenAI API keys).

OPENAI_API_KEY=your_api_key_here
```

### 4. Start PostgreSQL

```Ensure you have a local PostgreSQL instance running. Update the db_url in the code if needed.

Example:

# Start a Postgres container (optional)
docker run -d --name postgres -e POSTGRES_USER=ai -e POSTGRES_PASSWORD=ai -e POSTGRES_DB=ai -p 5532:5432 postgres
```

### 5. Run the App

```python app.py

Then open http://localhost:8000 in your browser to interact with the Playground.

Folder Structure

.
├── app.py                  # Main entry point
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
├── README.md      
```