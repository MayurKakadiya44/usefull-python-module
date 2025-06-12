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
