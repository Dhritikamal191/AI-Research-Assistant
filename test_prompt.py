from src.prompt import build_prompt

context = """
Document: AI.pdf
Page: 5

Retrieval-Augmented Generation (RAG) combines information retrieval with large language models.
"""

question = "What is RAG?"

prompt = build_prompt(context, question)

print(prompt)