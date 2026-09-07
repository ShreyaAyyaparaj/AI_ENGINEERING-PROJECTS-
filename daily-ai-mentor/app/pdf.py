from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem
)
from reportlab.lib.units import inch

from schemas.lesson import Lesson


OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def create_lesson_pdf(lesson: Lesson) -> Path:

    OUTPUT_DIR.mkdir(exist_ok=True)

    file_path = OUTPUT_DIR / f"lesson_day_{lesson.day}.pdf"

    print("\nCreating PDF...")
    print("PDF path:", file_path)

    document = SimpleDocTemplate(
        str(file_path),
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    story = []

    # Title
    story.append(
        Paragraph(
            f"Day {lesson.day}: {lesson.topic}",
            title_style
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    # Difficulty
    story.append(
        Paragraph(
            f"<b>Difficulty:</b> {lesson.difficulty}",
            body_style
        )
    )

    story.append(Spacer(1, 0.2 * inch))

    # Concept
    story.append(
        Paragraph("Concept", heading_style)
    )

    story.append(
        Paragraph(lesson.concept, body_style)
    )

    story.append(Spacer(1, 0.2 * inch))

    # Theory
    story.append(
        Paragraph("Theory", heading_style)
    )

    story.append(
        Paragraph(lesson.theory, body_style)
    )

    story.append(Spacer(1, 0.2 * inch))

    # Practical Task
    story.append(
        Paragraph("Practical Task", heading_style)
    )

    story.append(
        Paragraph(lesson.practical_task, body_style)
    )

    story.append(Spacer(1, 0.2 * inch))

    # Quiz
    story.append(
        Paragraph("Quiz", heading_style)
    )

    quiz_items = []

    for question in lesson.quiz:

        quiz_items.append(
            ListItem(
                Paragraph(
                    f"<b>{question.question}</b><br/>"
                    f"Answer: {question.answer}",
                    body_style
                )
            )
        )

    story.append(
        ListFlowable(
            quiz_items,
            bulletType="1"
        )
    )

    # Build PDF
    document.build(story)

    print("PDF creation completed.")

    return file_path