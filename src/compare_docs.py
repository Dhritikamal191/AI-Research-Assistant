"""
compare_docs.py
----------------
Compare two or more documents.
"""

from src.llm import generate_response


def compare_documents(documents):
    """
    Compare multiple documents.

    Parameters
    ----------
    documents : dict

    Example

    {
        "paper1.pdf": "...text...",
        "paper2.pdf": "...text..."
    }
    """

    if len(documents) < 2:
        return "Please upload at least two documents."

    prompt = """
You are an AI Research Assistant.

Compare the following documents.

For every document explain

1. Main Objective

2. Methodology

3. Strengths

4. Weaknesses

5. Similarities

6. Differences

7. Conclusion

"""

    for name, text in documents.items():

        prompt += f"""

===========================

Document

{name}

===========================

{text[:6000]}

"""

    return generate_response(prompt)