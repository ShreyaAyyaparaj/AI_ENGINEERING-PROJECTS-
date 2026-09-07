from pydantic import BaseModel, Field
from typing import Literal

class QuizzQuestion(BaseModel):
    question: str
    answer: str

class Lesson(BaseModel):
    day: int
    topic: str
    difficulty: Literal["beginner","intermediate","advanced"]
    concept: str
    theory: str
    practical_task: str
    quiz: list[QuizzQuestion]