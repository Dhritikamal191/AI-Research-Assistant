"""
summarizer.py
--------------
Document Summarization
"""

from src.llm import generate_response


def summarize_document(document_text, summary_type="Executive"):
    """
    Generate document summary.

    Parameters
    ----------
    document_text : str
        Full document text

    summary_type : str
        Executive
        Detailed
        Bullet
        Key Findings
    """

    if summary_type == "Executive":

        instruction = """
        Write an executive summary
        within 200 words.
        """

    elif summary_type == "Detailed":

        instruction = """
        Write a detailed summary.
        """

    elif summary_type == "Bullet":

        instruction = """
        Summarize using bullet points.
        """

    elif summary_type == "Key Findings":

        instruction = """
        List the important findings.
        """

    else:

        instruction = "Summarize."

    prompt = f"""

You are an AI Research Assistant.

{instruction}

Document:

{document_text}

"""

    return generate_response(prompt)