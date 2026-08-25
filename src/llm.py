"""
llm.py
------
LLM wrapper for the AI Research Assistant.

Uses:
- Groq API
- Llama 3.3 70B Versatile
"""

import os

from dotenv import load_dotenv
from groq import Groq


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError(
        "GROQ_API_KEY is not set. "
        "Please add it to your .env file or deployment environment."
    )


# ============================================================
# GROQ CLIENT
# ============================================================

client = Groq(
    api_key=API_KEY
)


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_NAME = "llama-3.3-70b-versatile"

DEFAULT_TEMPERATURE = 0.3

DEFAULT_MAX_TOKENS = 1024


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are an intelligent AI Research Assistant.

Your responsibilities:

1. Use uploaded documents as the PRIMARY source of information.

2. If the uploaded documents contain relevant information:
   - Answer using the document evidence.
   - Clearly explain the relevant information.
   - Mention the document name and page number when available.

3. If the uploaded documents do not contain enough information:
   - Use your general knowledge and reasoning to provide the best
     possible answer.
   - Clearly distinguish between information supported by the
     documents and information based on general knowledge or analysis.

4. For questions requiring:
   - interpretation,
   - comparison,
   - reasoning,
   - judgment,
   - authenticity assessment,
   - explanation,
   - or analysis,

   provide a reasoned answer even when the document does not
   explicitly contain the answer.

5. Never invent information.

6. Never claim that information is present in an uploaded document
   when it is not actually supported by the provided context.

7. When making an inference, clearly indicate that it is an
   inference or analytical conclusion.

8. If the question is completely unrelated to the uploaded
   documents, answer it normally using your general knowledge.

9. Keep answers clear, accurate, concise, and professional.

10. When document context is available, prioritize it over
    unsupported assumptions.
"""


# ============================================================
# MESSAGE BUILDER
# ============================================================

def build_messages(prompt: str):
    """
    Build the messages sent to the LLM.

    Parameters
    ----------
    prompt : str
        User prompt containing the question and, when available,
        retrieved document context.

    Returns
    -------
    list
        Messages compatible with the Groq chat completion API.
    """

    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ]


# ============================================================
# GENERATE RESPONSE
# ============================================================

def generate_response(
    prompt: str,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS
) -> str:
    """
    Generate a response using Llama 3.3 70B Versatile.

    Parameters
    ----------
    prompt : str
        Prompt containing the user question and RAG context.

    temperature : float
        Controls response creativity.

    max_tokens : int
        Maximum number of output tokens.

    Returns
    -------
    str
        Generated response.
    """

    if not prompt or not prompt.strip():
        return "Please enter a valid question."

    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=build_messages(
                prompt
            ),

            temperature=temperature,

            max_tokens=max_tokens

        )

        if not response.choices:
            return "The AI model returned an empty response."

        answer = (
            response
            .choices[0]
            .message
            .content
        )

        if not answer:
            return "The AI model returned an empty response."

        return answer.strip()

    except Exception as e:

        return (
            "LLM Error: "
            f"{str(e)}"
        )


# ============================================================
# STREAM RESPONSE
# ============================================================

def stream_response(
    prompt: str,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS
):
    """
    Stream an LLM response token-by-token.

    Parameters
    ----------
    prompt : str
        Prompt containing the user question and RAG context.

    temperature : float
        Controls response creativity.

    max_tokens : int
        Maximum number of output tokens.

    Yields
    ------
    str
        Individual response chunks.
    """

    if not prompt or not prompt.strip():

        yield "Please enter a valid question."

        return

    try:

        stream = client.chat.completions.create(

            model=MODEL_NAME,

            messages=build_messages(
                prompt
            ),

            temperature=temperature,

            max_tokens=max_tokens,

            stream=True

        )

        for chunk in stream:

            if not chunk.choices:
                continue

            content = (
                chunk
                .choices[0]
                .delta
                .content
            )

            if content:
                yield content

    except Exception as e:

        yield (
            "LLM Error: "
            f"{str(e)}"
        )


# ============================================================
# MODEL INFORMATION
# ============================================================

def get_model_info():
    """
    Return information about the configured LLM.

    Returns
    -------
    dict
        Model configuration information.
    """

    return {
        "provider": "Groq",
        "model": MODEL_NAME,
        "temperature": DEFAULT_TEMPERATURE,
        "max_tokens": DEFAULT_MAX_TOKENS
    }


# ============================================================
# COMMAND LINE TEST
# ============================================================

if __name__ == "__main__":

    print(
        "\n"
        + "=" * 60
    )

    print(
        "AI RESEARCH ASSISTANT - LLM TEST"
    )

    print(
        "=" * 60
    )

    print(
        f"Provider : Groq"
    )

    print(
        f"Model    : {MODEL_NAME}"
    )

    print(
        "=" * 60
    )

    question = input(
        "\nAsk a question: "
    ).strip()

    if not question:

        print(
            "Please enter a question."
        )

        raise SystemExit(1)

    print(
        "\nGenerating response...\n"
    )

    answer = generate_response(
        question
    )

    print(
        "=" * 60
    )

    print(
        "ANSWER"
    )

    print(
        "=" * 60
    )

    print(
        answer
    )

    print(
        "\n"
    )