# Multi-Agent-Stock-Advisor

# Multi-Agent Stock Advisor: Intelligent Financial Analysis Using LLMs

This project leverages multiple AI agents using the [`agno`](https://github.com/agronholm/agno) framework to perform financial market analysis and web research on publicly traded companies. It helps users make informed investment decisions by comparing companies like NVIDIA, Meta, and Google based on real-time financial data and market sentiment.

## 🧠 Project Overview

The system is composed of multiple intelligent agents, each with a specific role:

- **Web Agent**: Uses DuckDuckGo search to gather recent web-based insights and news articles with source attribution.
- **Finance Agent**: Fetches financial data (stock price, fundamentals, analyst recommendations) from Yahoo Finance and presents it in well-structured tables.
- **Team Agent**: Coordinates the other agents and combines their output for a comprehensive investment analysis.

## 📦 Dependencies

Make sure you have the following installed:

- Python 3.8+
- [`agno`](https://pypi.org/project/agno/)
- `python-dotenv`
- `.env` file with your API keys:
  ```dotenv
  GROQ_API_KEY=your_groq_api_key_here
