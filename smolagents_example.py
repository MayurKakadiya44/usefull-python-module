# Smolagents is an open-source, minimalist AI agent framework developed by Hugging Face, designed to simplify building and deploying AI agents that leverage Large Language Models (LLMs) for task automation. 
# The CodeAgent is a specific type of agent within the Smolagents framework that enables LLMs to generate and execute Python code to perform tasks, making it particularly useful for dynamic, multi-step workflows in generative AI applications. 
# Below, I’ll provide a detailed explanation of the CodeAgent, its architecture, capabilities, and practical examples, tailored to your interest in generative AI tools like Langfuse, Smolagents, and Whisper.

# The CodeAgent is a core component of the Smolagents framework, designed to allow LLMs to interact with external tools and systems by generating executable Python code. 
# Unlike traditional LLMs that produce text responses, CodeAgent empowers the model to write code that can perform actions such as calling APIs, processing data, or interacting with files and systems, all within a secure, sandboxed environment. 
# Its lightweight design (~1,000 lines of code) emphasizes simplicity, modularity, and compatibility with any LLM, including those from Hugging Face Hub, OpenAI, or Anthropic.

# Example 1: Data Analysis with CodeAgent
# Scenario: You want to analyze a CSV file containing sales data and calculate the total revenue for a specific product category (e.g., “Electronics”). The data is stored in sales.csv.

from smolagents import CodeAgent, HfApiModel
import pandas as pd

# Initialize LLM and CodeAgent
model = HfApiModel(model_id="mistralai/Mixtral-8x7B-Instruct-v0.1")
agent = CodeAgent(tools=[], model=model)

# Task
task = """
Analyze the CSV file 'sales.csv' with columns 'product_category', 'price', and 'quantity'.
Calculate the total revenue (price * quantity) for the 'Electronics' category.
Return the result in a final_answer function.
"""

# Run the agent
result = agent.run(task)

# Output
print(result)

# OP : Total revenue for Electronics: $12,500

# Generated Code by Agent (example):
# python

import pandas as pd
import matplotlib.pyplot as plt

def final_answer():
    df = pd.read_csv("data.csv")
    sales_by_category = df.groupby("category")["sales"].sum()
    sales_by_category.plot(kind="bar")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.title("Sales by Category")
    plt.savefig("sales_plot.png")
    return "sales_plot.png"



#=========================================================

# Example 2: Web Search for AI Articles
# Scenario: You want to fetch the top 3 URLs for recent AI articles using a web search tool, integrating with a tool like SerpAPI for search results.
                                                                                                                               
from smolagents import CodeAgent, HfApiModel
from smolagents.tools import WebSearchTool

# Initialize LLM and CodeAgent with WebSearchTool
model = HfApiModel(model_id="mistralai/Mixtral-8x7B-Instruct-v0.1")
web_search = WebSearchTool(api_key="your_serpapi_key")
agent = CodeAgent(tools=[web_search], model=model)

# Task
task = """
Use the WebSearchTool to search for recent AI articles.
Return the top 3 URLs in a final_answer function.
"""

# Run the agent
result = agent.run(task)

# Output
print(result)

# Output (example):

# [
#     "https://ai-news.com/article1",
#     "https://tech-blog.com/ai-trends",
#     "https://research.ai/paper"
# ]

#=========================================================

# Example 3: Voice-Driven Task with Whisper Integration
# Scenario: You want to transcribe a spoken command (“Search for flights to Tokyo next month”) using Whisper v3, then use CodeAgent to fetch flight data from an API (e.g., Skyscanner API mock).

from transformers import pipeline
from smolagents import CodeAgent, HfApiModel
import torch

# Initialize Whisper for transcription
device = "cuda" if torch.cuda.is_available() else "cpu"
whisper = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device=device)

# Initialize CodeAgent
model = HfApiModel(model_id="mistralai/Mixtral-8x7B-Instruct-v0.1")
agent = CodeAgent(tools=[FlightSearchTool()], model=model)

# Transcribe audio
audio = "flight_query.wav"
transcription = whisper(audio, generate_kwargs={"task": "transcribe", "language": "english"})
task = transcription["text"]

# Run CodeAgent
result = agent.run(task)

# Log to Langfuse
from langfuse import get_client
langfuse = get_client()
langfuse.trace(
    name="voice_flight_search",
    input=task,
    output=result,
    metadata={"audio": "flight_query.wav", "tool": "FlightSearchTool"}
)

# Output
print(result)  # op : Cheapest flight to Tokyo: ANA, $750, March 1, 2026


                                                                                                                               
                                                                                                                               


