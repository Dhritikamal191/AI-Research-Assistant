from src.llm import generate_response
from dotenv import load_dotenv
response = generate_response("What is Machine Learning?")

print(response)