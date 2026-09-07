from google import genai
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path
import os
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY  not found in .env")

client = genai.Client(api_key=api_key)

MODEL = 'gemini-2.5-flash'
PROMPT_A = """ Explain RAG"""
PROMPT_B = """You are an AI Engineering mentor teaching a beginner.

The learner already understands:
- tokens
- tokenization
- embeddings
- vectors
- cosine similarity

Explain Retrieval-Augmented Generation (RAG).

Your explanation must contain:

1. What RAG is
2. Why RAG is needed
3. The complete RAG pipeline
4. A practical example
5. A simple analogy
6. One common mistake beginners make
7. One practical exercise

Do not re-explain tokens, tokenization, or embeddings.

Keep the explanation technically accurate but beginner-friendly."""

# --------------------------------------------------
# Gemini call
# --------------------------------------------------

def generate_response(prompt):
    response = client.models.generate_content(
        model= MODEL,
        contents = prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
        )
    )
    return response


def main():
    print("="*50)
    print("DAY 4- PROMPT ENGINEERING EXPERIMENT")

    print("\n Running Prompt A...")

    response_A = generate_response(PROMPT_A)

    print("Prompt A completed")

    print("Prompt B...")
    response_B = generate_response(PROMPT_B)
    print("\n" + "=" * 80)
    print("PROMPT A RESPONSE")
    print("=" * 80)
    print(response_A.text)

    print("\n" + "=" * 80)
    print("PROMPT B RESPONSE")
    print("=" * 80)
    print(response_B.text)

    # --------------------------------------------------
    # Token usage
    # --------------------------------------------------

    print("\n\n")
    print("=" * 80)
    print("TOKEN USAGE")
    print("=" * 80)

    usage_a = response_A.usage_metadata
    usage_b = response_B.usage_metadata

    print("\nPROMPT A")

    print(
        "Input tokens:",
        getattr(usage_a, "prompt_token_count", 0)
    )

    print(
        "Output tokens:",
        getattr(usage_a, "candidates_token_count", 0)
    )

    print(
        "Total tokens:",
        getattr(usage_a, "total_token_count", 0)
    )

    print("\nPROMPT B")

    print(
        "Input tokens:",
        getattr(usage_b, "prompt_token_count", 0)
    )

    print(
        "Output tokens:",
        getattr(usage_b, "candidates_token_count", 0)
    )

    print(
        "Total tokens:",
        getattr(usage_b, "total_token_count", 0)
    )


if __name__ == "__main__":
    main()