"""
prompt.py
----------
Prompt templates for the AI Research Assistant (RAG)
"""

SYSTEM_PROMPT = """
You are an AI Research Assistant.

Your responsibilities:
1. Answer ONLY using the provided document context.
2. Do NOT make up facts or hallucinate information.
3. If the answer cannot be found in the context, reply:
   "I don't know based on the uploaded documents."
4. Explain the answer clearly and professionally.
5. Mention the source document name and page number whenever available.
6. Keep the answer concise but informative.
"""


def build_prompt(context: str, question: str) -> str:
    """
    Build the prompt sent to the LLM.

    Parameters
    ----------
    context : str
        Retrieved text chunks from the vector database.

    question : str
        User's question.

    Returns
    -------
    str
        Complete prompt.
    """

    prompt = f"""
{SYSTEM_PROMPT}

=========================
DOCUMENT CONTEXT
=========================

{context}

=========================
USER QUESTION
=========================

{question}

=========================
INSTRUCTIONS
=========================

Answer ONLY from the document context.

If the context does not contain enough information, reply exactly:

"I don't know based on the uploaded documents."

When possible include:

• Document Name
• Page Number

Provide a clear, professional answer.

Answer:
"""

    return prompt 