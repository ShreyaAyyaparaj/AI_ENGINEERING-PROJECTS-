from llm import generate_lesson
from prompts import DAILY_LESSON_PROMPT
from pdf import create_lesson_pdf
from emailer import send_email
def main():

    topic = "Structured Outputs and Pydantic"

    prompt = DAILY_LESSON_PROMPT.format(
        topic=topic
    )

    lesson = generate_lesson(prompt)
    pdf_path = create_lesson_pdf(lesson)

    print("\nPDF saved to:")
    print(pdf_path)

    send_email(
    subject=f"Daily AI Mentor — Day {lesson.day}",
    body=f"""
    Here is your AI Engineering lesson for Day {lesson.day}.

    Topic: {lesson.topic}

    Your lesson PDF is attached.

    Keep buildi
    ng!
    """,
        attachment_path=pdf_path
    )

    print("\nEmail sent successfully.")

    print("=" * 70)
    print("DAILY AI MENTOR")
    print("=" * 70)

    print("\nDay:", lesson.day)
    print("Topic:", lesson.topic)
    print("Difficulty:", lesson.difficulty)

    print("\nConcept:")
    print(lesson.concept)

    print("\nTheory:")
    print(lesson.theory)

    print("\nPractical Task:")
    print(lesson.practical_task)

    print("\nQuiz:")

    for i, question in enumerate(lesson.quiz, start=1):

        print(f"\n{i}. {question.question}")
        print(f"Answer: {question.answer}")


if __name__ == "__main__":
    main()