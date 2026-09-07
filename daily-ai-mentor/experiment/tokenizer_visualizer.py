from transformers import AutoTokenizer
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

env_load = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_load)
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key = api_key)

Model = "gemini-2.5-flash"
def main():

    text = "AI is transforming the world."

    print("="*55)
    print("Tokenization Visualizer")
    print("="*55)

    print("\n Text:")
    print(text)
    tokenzier = AutoTokenizer.from_pretrained("bert-base-uncased")

    token_id = tokenzier.encode(text, add_special_tokens=False)

    print("\n Token IDs:")
    print(token_id)


    tokens = tokenzier.convert_ids_to_tokens(token_id)
    print("\n Tokens:")
    print(tokens)

    print("\n Token count:", len(tokens))

    print("\n" + "="*55)

if __name__ == "__main__":
    main()

