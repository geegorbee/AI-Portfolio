# prompt_tester.py

# NOTE: This is a placeholder script designed for demonstration purposes.
# In real use, you would import and use an API like OpenAI's GPT model.

import csv
from datetime import datetime

# Sample prompt list
prompts = [
    "Explain reinforcement learning to a 12-year-old.",
    "Write a formal apology email to a customer whose order was delayed.",
    "List three benefits and three drawbacks of using AI in public health.",
]

# Simulated model responses (replace with actual LLM calls)
responses = [
    "Reinforcement learning is like teaching a dog new tricks using treats...",
    "Dear Customer, We sincerely apologize for the delay in your order...",
    "Benefits: efficiency, data insight, scalability. Drawbacks: bias, privacy, cost."
]

# Write to CSV for evaluation
with open("sample_results.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Prompt", "Response"])
    for i in range(len(prompts)):
        writer.writerow([datetime.now().isoformat(), prompts[i], responses[i]])

print("Sample prompts and responses written to sample_results.csv")