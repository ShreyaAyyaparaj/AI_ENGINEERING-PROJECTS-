from google import genai
from dotenv import load_dotenv
import os
from pathlib import Path

env_load = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_load)
api_key = os.getenv("GOOGLE_API_KEY")


if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in the .env file.")

client = genai.Client(api_key=api_key)

def main():
    text = "Artificial Intelligence is transforming the world."
    print("="*60)
    print("Embedding Experiment")
    print("="*60)

    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents = text
    )

    embedding = result.embeddings[1].values # type: ignore

    print("\nEmbeddings:", embedding)

    if embedding is None:
        raise ValueError("Embedding values were not returned.")

    print("\nEmbedding Length:", len(embedding))

if __name__ =="__main__":
    main()
