from google import genai
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path
import os
from schemas.lesson import Lesson

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API KEY NOT FOUND!!!")

client = genai.Client(api_key=api_key)

MODEL = 'gemini-2.5-flash'

PROMPT = """
You are an AI Engineering mentor.

Create today's learning lesson for a beginner
learning AI Engineering.

Today's topic is:

Structured Outputs and Pydantic.

The learner already understands:
- APIs
- Gemini API
- tokens
- embeddings
- vectors
- cosine similarity
- basic prompt engineering

Create a practical lesson.

Include:
- what structured outputs are
- why they are useful
- how they work
- one practical example
- one exercise
- three quiz questions

Keep the lesson beginner-friendly.
"""


def main():
    print("=" *70)
    print("DAY 6 - STRUCTURED OUTPUT EXPERIMENT!!")
    print("=" * 70)

    response = client.models.generate_content(
        model=MODEL,
        contents=PROMPT,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Lesson,
            temperature = 0.3
        )
    )

    print("\nRaw response:")

    print(response.text)
    if response.text is None:
        raise ValueError("Response text is empty")

    lesson = Lesson.model_validate_json(response.text)

    print("\n" + "=" * 70)
    print("VALIDATED LESSON")
    print("=" * 70)

    print("\nTopic:")
    print(lesson.topic)

    print("\nDifficulty:")
    print(lesson.difficulty)

    print("\nConcept:")
    print(lesson.concept)

    print("\nPractical Task:")
    print(lesson.practical_task)

    print("\nQuiz:")

    for index, question in enumerate(lesson.quiz, start=1):

        print(f"\n{index}. {question.question}")
        print(f"Answer: {question.answer}")

if __name__ == "__main__":
    main()
