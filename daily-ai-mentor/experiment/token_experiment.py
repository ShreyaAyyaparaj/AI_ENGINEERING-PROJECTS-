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
    prompt = input("You:")

    print("=" *45)
    print("AI Token Experiment")
    print("="*45)

    print("\n Prompt:")
    print(prompt)


    token_response = client.models.count_tokens(
        model = Model,
        contents = prompt
    )
    input_tokens = token_response.total_tokens

    print("\n Input Tokens:", input_tokens)

    response = client.models.generate_content(
        model = Model,
        contents = prompt
    )
    print("\n Gemini Response:", response.text)

    
    usage = response.usage_metadata
    print("\n" + "=" * 50)
    print("TOKEN USAGE")
    print("=" * 50)

    input_tokens = getattr(usage, "prompt_token_count", 0) or 0
    output_tokens = getattr(usage, "candidates_token_count", 0) or 0
    total_tokens = getattr(usage, "total_token_count", 0) or 0

    print("Input tokens :", input_tokens)
    print("Output tokens:", output_tokens)
    print("Total tokens :", total_tokens)

if __name__ == "__main__":
    main()