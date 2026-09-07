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

MODEL = "gemini-2.5-flash"


def generate_lesson(prompt: str) -> Lesson:

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Lesson,
            temperature=0.3,
        ),
    )
    if response.text is None:
        raise ValueError("Response text is empty")


    lesson = Lesson.model_validate_json(response.text)

    return lesson