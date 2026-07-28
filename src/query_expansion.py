def expand_query(question):
    """
    Generate lightweight alternative search queries.

    This version does not call the LLM, so it doesn't consume
    additional Groq tokens.
    """

    question = question.strip()

    queries = [
        question,
        f"Detailed information about {question}",
        f"Requirements and conditions related to {question}",
    ]

    # Remove duplicates while preserving order
    return list(dict.fromkeys(queries))