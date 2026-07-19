"""
llm.py
-------
LLM wrapper for the AI Research Assistant.

Uses:
- Groq API
- Llama 3.3 70B Versatile
"""

from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if API_KEY is None:
   raise ValueError("GROQ_API_KEY is not found in .env file.")

client = Groq(api_key= API_KEY)

def generate_response(prompt: str,temperature: float = 0.3,max_tokens: int = 1024) -> str:
    """
    Generate a response using Llama 3.

    Parameters
    ----------
    prompt : str
        Prompt sent to the model.

    temperature : float
        Controls creativity.

    max_tokens : int
        Maximum output tokens.

    Returns
    -------
    str
        Generated response.
    """

    try:
        response = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "system", "content": ("You are an AI Research Assistant." "Answer clearly, accurately, and professionally." "Use only the provided document context whenever available." "If the answer is not in the context, say" "'I don't know based on the uploaded documents.'"),},{"role": "user", "content": prompt,},], temperature=temperature, max_tokens=max_tokens,)
        return response.choices[0].message.content.strip()
  
    except Exception as e:
           return f"LLM Error: {str(e)}"

def stream_response(prompt,temperature=0.3,max_tokens=1024):

    stream = client.chat.completions.create(model="llama-3.3-70b-versatile",messages=[{"role":"user","content":prompt}],stream=True,temperature=temperature,max_tokens=max_tokens)

    for chunk in stream:

        if chunk.choices[0].delta.content:

            yield chunk.choices[0].delta.content
